from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from notifications.models import Notification

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
        Notification.objects.filter(
            sender=request.user,
            recipient=post.user,
            notif_type='like',
            post=post
        ).delete()
    else:
        post.likes.add(request.user)
        if request.user != post.user:
            Notification.objects.get_or_create(
                sender=request.user,
                recipient=post.user,
                notif_type='like',
                post=post
            )
    return redirect('feed')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
        messages.success(request, 'Post deleted!')
    return redirect('feed')

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
    })

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content.strip():
            Comment.objects.create(user=request.user, post=post, content=content)
            if request.user != post.user:
                Notification.objects.create(
                    sender=request.user,
                    recipient=post.user,
                    notif_type='comment',
                    post=post
                )
    return redirect('post_detail', post_id=post_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if comment.user == request.user:
        comment.delete()
    return redirect('post_detail', post_id=post_id)