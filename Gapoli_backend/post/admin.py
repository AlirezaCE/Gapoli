from django.contrib import admin
from .models import PostAttachment, Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_by', 'created_at') 
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_by', 'like_count', 'comment_count') 


admin.site.register(Post, PostAdmin)
admin.site.register(PostAttachment)
admin.site.register(Comment, CommentAdmin)