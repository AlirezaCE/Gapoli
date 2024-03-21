from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q

from .models import Conversation, ConversationMessage
from .serializers import ConversationMessageSerializer, ConversationSerializer, ConversationDetailSerializer
from account.models import User, FriendshipRequest
from account.models import SENT, ACCEPTED, REJECTED
from .forms import ConversationMessageForm


@api_view(['GET'])
def conversation_list(request):   
    user = request.user
    conversations = Conversation.objects.filter(users__in=list([user]))
    serializer = ConversationSerializer(conversations, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def conversation_detail(request, id):   
    user = request.user
    conversation = Conversation.objects.filter(users__in=list([user])).get(id=id)
    serializer = ConversationDetailSerializer(conversation)
    
    return JsonResponse(serializer.data, safe=False)
    

@api_view(['POST'])
def send_message(request, id):
    form = ConversationMessageForm(request.data)

    if form.is_valid():
        sender = request.user
        conversation = Conversation.objects.get(id=id)
        conversation_message = form.save(commit=False)
        conversation_message.conversation = conversation
        conversation_message.sender = sender
        for user in conversation.users.all():
            if user != sender:
                conversation_message.reciver = user
                conversation_message.save()        
        serializer = ConversationMessageSerializer(conversation_message)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': "form is not valid"})
