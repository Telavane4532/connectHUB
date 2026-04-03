from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message

@login_required
def inbox(request):
    # Get all users who have exchanged messages with current user
    messages_qs = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    )
    # Get unique users from conversations
    user_ids = set()
    for msg in messages_qs:
        if msg.sender != request.user:
            user_ids.add(msg.sender.id)
        if msg.recipient != request.user:
            user_ids.add(msg.recipient.id)

    conversation_users = User.objects.filter(id__in=user_ids)

    # Unread count
    unread_count = Message.objects.filter(
        recipient=request.user, is_read=False
    ).count()

    return render(request, 'messaging/inbox.html', {
        'conversation_users': conversation_users,
        'unread_count': unread_count,
    })

@login_required
def conversation(request, username):
    other_user = get_object_or_404(User, username=username)
    # Get all messages between the two users
    msgs = Message.objects.filter(
        Q(sender=request.user, recipient=other_user) |
        Q(sender=other_user, recipient=request.user)
    ).order_by('created_at')

    # Mark received messages as read
    msgs.filter(recipient=request.user).update(is_read=True)

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Message.objects.create(
                sender=request.user,
                recipient=other_user,
                content=content
            )
        return redirect('conversation', username=username)

    return render(request, 'messaging/conversation.html', {
        'other_user': other_user,
        'msgs': msgs,
    })