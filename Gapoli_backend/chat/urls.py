from django.urls import path
from .views import conversation_list

urlpatterns = [
    path('', conversation_list, name='conversation_list'),
]
