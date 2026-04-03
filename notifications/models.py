from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    NOTIF_TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.recipient} ({self.notif_type})"