from django.urls import path
from .views import conversation_list, conversation_detail, send_message, create_direct_conversation

urlpatterns = [
    path('', conversation_list, name='conversation_list'),
    path('<uuid:id>/<str:id_type>/', conversation_detail, name='conversation_detail'),
    path('send/<uuid:id>/', send_message, name='send_message'),
    path('start_direct/', create_direct_conversation, name='create_direct_conversation'),
]
