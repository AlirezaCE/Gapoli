from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q

from .models import Post, PostAttachment, Like
from .serializers import PostSerializer, PostDetailSerializer
from .forms import PostForm
from account.models import User, FriendshipRequest
from account.models import SENT, ACCEPTED, REJECTED
from account.serializers import UserSerializer


@api_view(['GET'])
def post_list(request):    
    current_user = request.user
    
    posts = Post.objects.filter(Q(created_by=current_user) | Q(created_by__in=current_user.friends.all()))
    serializer = PostSerializer(posts, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def post_detail(request, id):        
    posts = Post.objects.get(id=id)
    serializer = PostDetailSerializer(posts)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def user_post_profile(request, id):
    user = User.objects.get(pk = id)
    posts = Post.objects.filter(created_by_id = id)
    friendshipButtonText =''

    friendshipButtonText = getFriendshipButtonText(request.user, user)
        
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    
    return JsonResponse({
        'post': post_serializer.data,
        'user': user_serializer.data,
        'friendshipButtonText': friendshipButtonText
        }, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': "form is not valid"})
    
    
@api_view(['POST'])
def post_like(request, id):    
    post = Post.objects.get(id=id)
    
    if not post.like.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)
        
        post.like_count += 1
        post.like.add(like)
        post.save()

        return JsonResponse({'message': 'like'}, safe=False)   
    else:        
        like = Like.objects.get(created_by=request.user)
        
        post.like_count -= 1
        post.like.remove(like)
        like.delete()
        
        post.save()
        
        return JsonResponse({'message': 'takeback'})
    
    
def getFriendshipButtonText(user1, user2):
    if FriendshipRequest.objects.filter(sender=user1, reciver=user2, status=SENT).exists():
        return 'cancel friendship request'
    elif FriendshipRequest.objects.filter(sender=user2, reciver=user1, status=SENT).exists():
        return 'asked to be friend'
    elif FriendshipRequest.objects.filter(sender=user1, reciver=user2, status=ACCEPTED).exists() or \
         FriendshipRequest.objects.filter(sender=user2, reciver=user1, status=ACCEPTED).exists():
        return 'friend'
    elif FriendshipRequest.objects.filter(sender=user1, reciver=user2, status=REJECTED).exists() or \
         FriendshipRequest.objects.filter(sender=user2, reciver=user1, status=REJECTED).exists():
        return 'rejected'
    else:
        return 'send firendship request'