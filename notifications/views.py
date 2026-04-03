from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications_view(request):
    notifs = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')
    # Mark all as read
    notifs.update(is_read=True)
    return render(request, 'notifications/notifications.html', {'notifs': notifs})