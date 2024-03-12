from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import signup, detail, friendship_request, firends_list, friendship_response

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signup, name='signup'),
    path('detail/', detail, name='detail'),
    path('friends/<uuid:id>/', firends_list, name='firends_list'),
    path('friends/<uuid:id>/request/', friendship_request, name='friendship_request'),
    path('friends/<uuid:id>/<str:status>/', friendship_response, name='friendship_request'),
]
