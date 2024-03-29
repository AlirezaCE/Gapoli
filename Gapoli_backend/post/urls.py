from django.urls import path
from .views import post_list, post_create, user_post_profile

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('profile/<uuid:id>/', user_post_profile, name='user_post_profile'),
]
