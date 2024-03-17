from django.urls import path
from .views import post_list, post_create, user_post_profile, post_like, post_detail, post_comment, post_comment_delete
urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('profile/<uuid:id>/', user_post_profile, name='user_post_profile'),
    path('like/<uuid:id>/', post_like, name='post_like'),
    path('detail/<uuid:id>/', post_detail, name='post_detail'),
    path('comment/<uuid:id>/', post_comment, name='post_comment'),
    path('comment/delete/<uuid:p_id>/<uuid:c_id>/', post_comment_delete, name='post_comment_delete'),
]
