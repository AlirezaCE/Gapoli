from django.contrib import admin
from .models import PostAttachment, Post, Comment, Like


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_by', 'created_at') 
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_by', 'like_count', 'comment_count') 

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by') 


admin.site.register(Post, PostAdmin)
admin.site.register(PostAttachment)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)