from django.db import models
import uuid
from django.utils import timezone

from account.models import User



class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

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


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attachment = models.ImageField(upload_to='post_attachments')
#    created_by = models.ForeignKey(User, related_name='post_attachments', on_deleted=models.CASCADE)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField(PostAttachment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    like = models.ManyToManyField(Like, blank=True)
    like_count = models.IntegerField(default=0)
    comment = models.ManyToManyField(Comment, blank=True)
    comment_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('-created_at',)
        
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
