from django.db import models
import uuid
from django.utils import timezone

from account.models import User

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def since_modified(self):
        total_seconds = (timezone.now() - self.created_at).total_seconds()

        years = int(total_seconds // 31536000)        

        if years > 0:
            return f"{years} year{'s' if years > 1 else ''}"
        
        else:
            days = int(total_seconds // 86400)        
            if days > 0:
                return f"{days} day{'s' if days > 1 else ''}"
            
            else:
                hours = int(total_seconds // 3600)
                if hours > 0:
                    return f"{hours} hour{'s' if hours > 1 else ''}"
                
                else:
                    minutes = int(total_seconds // 60)
                    
                    if minutes > 0:
                        return f"{minutes} minute{'s' if minutes > 1 else ''}"
                    else:
                        return "just posted" 
                    
                        
class ConversationMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name='message_reciver', on_delete=models.CASCADE)

    def since_created(self):
        total_seconds = (timezone.now() - self.created_at).total_seconds()

        years = int(total_seconds // 31536000)        

        if years > 0:
            return f"{years} year{'s' if years > 1 else ''}"
        
        else:
            days = int(total_seconds // 86400)        
            if days > 0:
                return f"{days} day{'s' if days > 1 else ''}"
            
            else:
                hours = int(total_seconds // 3600)
                if hours > 0:
                    return f"{hours} hour{'s' if hours > 1 else ''}"
                
                else:
                    minutes = int(total_seconds // 60)
                    
                    if minutes > 0:
                        return f"{minutes} minute{'s' if minutes > 1 else ''}"
                    else:
                        return "just posted" 