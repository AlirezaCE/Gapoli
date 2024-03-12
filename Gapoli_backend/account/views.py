from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .form import SingupForm
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
    
    if FriendshipRequest.objects.filter(reciver=user_reciver, sender=request.user).exists():
        return JsonResponse({'message': 'exist'})
    else:
        FriendshipRequest.objects.create(reciver=user_reciver, sender=request.user)
        return JsonResponse({'message': 'successful'})



@api_view(['POST'])
def friendship_response(request, id, status): 
    sender = User.objects.get(id=id)   
    reciver = request.user
    
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
        
    return JsonResponse({'message': f"request for friendship is {status}"})
