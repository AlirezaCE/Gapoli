from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .form import SingupForm
from .models import User, FriendshipRequest


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


@api_view(['POST'])
def friendship_request(request, id):
    user_reciver = User.objects.get(pk=id)
    
    friendship_request = FriendshipRequest(reciver=user_reciver, sender=request.user)

    return JsonResponse({'message': 'friendship request was successful'})