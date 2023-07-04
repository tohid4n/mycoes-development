from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"From: {self.user.username}"

    class Meta:
        ordering = ('timestamp',)
        
        
class AdminMessage(models.Model):
    chat_message = models.ForeignKey(ChatMessage, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admin Message"

    class Meta:
        ordering = ('timestamp',)        