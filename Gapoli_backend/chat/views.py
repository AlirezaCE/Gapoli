from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q, Count

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
def conversation_detail(request, id, id_type):   
    user = request.user

    if id_type == 'conversation':
        if Conversation.objects.filter(users__in=list([user])).get(id=id):
            conversation = Conversation.objects.filter(users__in=list([user])).get(id=id)   
            serializer = ConversationDetailSerializer(conversation)
            
            return JsonResponse(serializer.data, safe=False) 
        
    elif id_type == 'reciver':
        reciver = User.objects.get(id=id)
        users = [user, reciver]
        existing_conversation = Conversation.objects.filter(
                users__in=users
            ).annotate(num_users=Count('users')).filter(num_users=len(users)).first()
        
        if existing_conversation:
            serializer = ConversationDetailSerializer(existing_conversation)
            
            return JsonResponse(serializer.data, safe=False)
    
    else:
            return JsonResponse("not found", safe=False)
            

@api_view(['POST'])
def send_message(request, id):
    form = ConversationMessageForm(request.data)

    if form.is_valid():
        sender = request.user
        conversation = Conversation.objects.filter(users__in=list([sender])).get(id=id)
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


@api_view(['POST'])
def create_direct_conversation(request):
    user = request.user
    reciver_id = request.data.get('reciver_id')
    reciver = User.objects.get(id=reciver_id)
    
    users = [user, reciver]
    
    existing_conversation = Conversation.objects.filter(
        users__in=users
    ).annotate(num_users=Count('users')).filter(num_users=len(users)).first()

    if existing_conversation:
        return JsonResponse({'message': 'exists'})
    
    new_conversation = Conversation.objects.create()
    new_conversation.users.add(*users)
    
    return JsonResponse({'message': 'created'})