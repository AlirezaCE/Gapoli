from django.contrib import admin
from .models import Conversation, ConversationMessage


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at') 
    
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_at', 'sender', 'reciver') 
    
    
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(ConversationMessage, ConversationMessageAdmin)

