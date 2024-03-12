from .models import User, FriendshipRequest
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'email', 'friends_count',]
        
class FriendshipRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = FriendshipRequest
        fields = ['id', 'sender',]