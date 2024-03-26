from django.contrib import admin
from .models import Conversation, ConversationMessage


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at', 'user_emails', 'user_names')

    def user_emails(self, obj):
        return ", ".join([user.email for user in obj.users.all()])
    user_emails.short_description = 'User Emails'
    
    def user_names(self, obj):
        return ", ".join([user.name for user in obj.users.all()])
    user_names.short_description = 'User Names'
    
    
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_at', 'sender', 'reciver') 
    
    
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(ConversationMessage, ConversationMessageAdmin)

