from django.urls import path
from .views import RegisterView, UserAPIView, LoginObtainTokenView

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('user/', UserAPIView.as_view(), name='user'),
  path('login/', LoginObtainTokenView.as_view(), name='login')
  
]
