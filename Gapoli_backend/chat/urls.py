from django.urls import path
from .views import conversation_list, conversation_detail, send_message

urlpatterns = [
    path('', conversation_list, name='conversation_list'),
    path('<uuid:id>/', conversation_detail, name='conversation_detail'),
    path('send/<uuid:id>/', send_message, name='send_message'),
]
