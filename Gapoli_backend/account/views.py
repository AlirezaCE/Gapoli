from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SingupForm
from .models import User, FriendshipRequest
from .models import SENT, ACCEPTED, REJECTED
from .serializers import UserSerializer, FriendshipRequestSerializer

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SingupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
        message = 'error'
    
    return JsonResponse({'status': message})


@api_view(['GET'])
def detail(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['GET'])
def firends_list(request, id):
    user = User.objects.get(pk=id)
    
    requests = []
    if user==request.user:
        requests = FriendshipRequest.objects.filter(reciver=user, status=SENT)

    friends = user.friends.all()
    
    return JsonResponse({
        'user':UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': FriendshipRequestSerializer(requests, many=True).data,
    }, safe=False)


@api_view(['POST'])
def friendship_request(request, id):
    user_reciver = User.objects.get(pk=id)
    
    if FriendshipRequest.objects.filter(reciver=user_reciver, sender=request.user, status=SENT).exists():
        FriendshipRequest.objects.filter(reciver=user_reciver, sender=request.user, status=SENT).delete()
        return JsonResponse({'message': 'canceled'})
    elif FriendshipRequest.objects.filter(reciver=user_reciver, sender=request.user, status=ACCEPTED).exists() or \
         FriendshipRequest.objects.filter(reciver=request.user, sender=user_reciver, status=ACCEPTED).exists():
        delete_friendship(request.user, user_reciver)
        return JsonResponse({'message': 'canceled_friendship'})
    elif FriendshipRequest.objects.filter(reciver=request.user, sender=user_reciver, status=SENT).exists():
        friendship_response_func(sender=user_reciver, reciver=request.user, status=ACCEPTED)
        return JsonResponse({'message': ACCEPTED})
    elif FriendshipRequest.objects.filter(reciver=user_reciver, sender=request.user, status=REJECTED):
        friendshipRequest = FriendshipRequest.objects.get(reciver=user_reciver, sender=request.user, status=REJECTED)
        friendshipRequest.status = SENT
        friendshipRequest.save()
        return JsonResponse({'message': 'sent'})
    elif FriendshipRequest.objects.filter(reciver=request.user, sender=user_reciver, status=REJECTED):
        friendshipRequest = FriendshipRequest.objects.get(reciver=request.user, sender=user_reciver, status=REJECTED)
        friendshipRequest.status = SENT
        friendshipRequest.save()        
        return JsonResponse({'message': 'sent'})
    else:
        FriendshipRequest.objects.create(reciver=user_reciver, sender=request.user)
        return JsonResponse({'message': 'sent'})



@api_view(['POST'])
def friendship_response(request, id, status): 
    sender = User.objects.get(id=id)   
    reciver = request.user
    if FriendshipRequest.objects.filter(reciver=reciver, sender=sender, status=SENT).exists():
        friendship_response_func(sender=sender, reciver=reciver, status=status)
        return JsonResponse({'message': status, 'sender':UserSerializer(sender).data})
    return JsonResponse({'message': 'exist'})    


def friendship_response_func(sender, reciver, status): 
    friendship_request = FriendshipRequest.objects.filter(reciver=reciver).get(sender=sender)
    friendship_request.status = status
    friendship_request.save()
    
    if status == ACCEPTED:
        sender.friends.add(reciver)
        sender.friends_count += 1
        sender.save()
        
        reciver.friends.add(sender)
        reciver.friends_count += 1        
        reciver.save()

def delete_friendship(user1,user2):
    if FriendshipRequest.objects.filter(reciver=user1, sender=user2).exists():
        FriendshipRequest.objects.filter(reciver=user1, sender=user2).delete()
    if FriendshipRequest.objects.filter(reciver=user2, sender=user1).exists():
        FriendshipRequest.objects.filter(reciver=user2, sender=user1).delete()
    
    user1.friends.remove(user2)
    user1.friends_count -= 1
    user1.save()
    user2.friends.remove(user1)
    user2.friends_count -= 1
    user2.save()