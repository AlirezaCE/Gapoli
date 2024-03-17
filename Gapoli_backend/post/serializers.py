from .models import Post, Comment
from rest_framework import serializers
from account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id','body','since_created','comment_count','created_by','like_count']
     
        
class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id','text','since_created','created_by']


class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comment = CommentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id','body','since_created','created_by','like_count','comment','comment_count']