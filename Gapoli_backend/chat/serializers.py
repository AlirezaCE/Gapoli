from .models import Conversation, ConversationMessage
from rest_framework import serializers
from account.serializers import UserSerializer



class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Conversation
        fields = ['id','users','since_modified']
     
class ConversationMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    reciver = UserSerializer(read_only=True)
    conversation = ConversationSerializer(read_only=True)
    
    class Meta:
        model = ConversationMessage
        fields = ['id','conversation','body','since_created','sender','reciver']
     
class ConversationDetailSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    messages = ConversationMessageSerializer(read_only=True)
    
    class Meta:
        model = Conversation
        fields = ['id','users','since_modified','messages']