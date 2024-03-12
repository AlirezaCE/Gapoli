from django.contrib import admin
from .models import User, FriendshipRequest


class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'reciver', 'sender') 
    
    
admin.site.register(User)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)

