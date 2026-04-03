from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile
from posts.models import Post

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('feed')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=profile_user)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    is_following = profile.followers.filter(id=request.user.id).exists()
    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
        'is_following': is_following,
    })

@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        profile.bio = bio
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        messages.success(request, 'Profile updated!')
        return redirect('profile', username=request.user.username)
    return render(request, 'accounts/edit_profile.html', {'profile': profile})

@login_required
def follow_user(request, username):
    from notifications.models import Notification
    target_user = get_object_or_404(User, username=username)
    target_profile, _ = Profile.objects.get_or_create(user=target_user)
    if request.user in target_profile.followers.all():
        target_profile.followers.remove(request.user)
        Notification.objects.filter(
            sender=request.user,
            recipient=target_user,
            notif_type='follow'
        ).delete()
    else:
        target_profile.followers.add(request.user)
        if request.user != target_user:
            Notification.objects.get_or_create(
                sender=request.user,
                recipient=target_user,
                notif_type='follow'
            )
    return redirect('profile', username=username)

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = User.objects.filter(
            username__icontains=query
        ).exclude(id=request.user.id)
    return render(request, 'accounts/search.html', {
        'results': results,
        'query': query,
    })