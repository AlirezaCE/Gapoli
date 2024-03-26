from django.urls import path
from .views import conversation_list, conversation_detail, send_message, create_direct_conversation, get_conversation_by_reciver_id

urlpatterns = [
    path('', conversation_list, name='conversation_list'),
    path('<uuid:id>/', conversation_detail, name='conversation_detail'),
    path('send/<uuid:id>/', send_message, name='send_message'),
    path('start_direct/', create_direct_conversation, name='create_direct_conversation'),
    path('get_conv_reciver_id/<uuid:id>/', get_conversation_by_reciver_id, name='get_conversation_by_reciver_id'),
]
