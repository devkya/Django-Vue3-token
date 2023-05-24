from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class RegisterView(APIView):
  permission_classes = [permissions.AllowAny,]

  def post(self, request):
    try:
      # payload data
      data = request.data
      first_name = data['first_name']
      last_name = data['last_name']
      username = data['username']
      password = data['password']
      re_password = data['re_password']
      
      # validation => 왜 여기서 처리하려고 하지?
      if password == re_password:
        if len(password)>= 8: 
          if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
              first_name = first_name,
              last_name = last_name,
              username = username,
              password = password,
            )
            user.save()
            return Response({'success' : "회원가입 완료"}, status=status.HTTP_201_CREATED)  
          else:
            return Response({'error' : "사용자가 이미 존재함"}, status=status.HTTP_400_BAD_REQUEST)  
        else:
          return Response({'error' : "Password가 8글자 미만임"}, status=status.HTTP_400_BAD_REQUEST)  
      else:
        return Response({'error' : "Password가 일치하지 않음"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print(e)
      return Response({'error' : '무엇인가 잘못 되었음'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
      
class UserAPIView(APIView):
  def get(self, request):
    try:
      user = request.user
      user = UserSerializer(user)
      return Response({'user':user.data}, status=status.HTTP_200_OK)
      
    except:
      return Response({'error' : '무엇인가 잘못 되었음'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  
class LoginObtainTokenView(TokenObtainPairView):
   def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Get the token from the response
        access = response.data['access']
        refresh = response.data['refresh']
        # Set the token as a cookie in the response
        response.set_cookie('access', access, httponly=True, path='/api/')
        response.set_cookie('refresh', refresh, httponly=True, path='/api/')

        # Return the response
        return response
    
