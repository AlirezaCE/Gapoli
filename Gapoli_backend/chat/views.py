from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q

from .models import Conversation, ConversationMessage
from .serializers import ConversationMessageSerializer, ConversationSerializer, ConversationDetailSerializer
from account.models import User, FriendshipRequest
from account.models import SENT, ACCEPTED, REJECTED


@api_view(['GET'])
def conversation_list(request):   
    user = request.user
    conversations = Conversation.objects.filter(users__in=list([user]))
    serializer = ConversationSerializer(conversations, many=True)
    
    return JsonResponse(serializer.data, safe=False)
    