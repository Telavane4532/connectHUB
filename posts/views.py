from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content.strip():
            Post.objects.create(user=request.user, content=content)
            messages.success(request, 'Post created!')
        else:
            messages.error(request, 'Post cannot be empty!')
    return redirect('feed')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
        messages.success(request, 'Post deleted!')
    return redirect('feed')