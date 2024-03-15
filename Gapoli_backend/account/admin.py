from django.contrib import admin
from .models import User, FriendshipRequest


class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'reciver', 'sender') 
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'friends_count', 'is_superuser') 
    
    
admin.site.register(User, UserAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)

