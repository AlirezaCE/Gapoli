from django.db import models
from account.models import User

class Conversation(models.Model):
    users = models.ManyToManyField(User, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
class ConversationMessge(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name='message_reciver', on_delete=models.CASCADE)
