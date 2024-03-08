from .models import Post
from rest_framework import serializers
from account.serializers import UserNameSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserNameSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id','body','since_created','created_by']