from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(APIView):
  permission_classes = [permissions.AllowAny,]

  def post(self, request):
    try:
      # payload data
      data = request.data
      email = data['email']
      first_name = data['first_name']
      last_name = data['last_name']
      username = data['username']
      password = data['password']
      re_password = data['re_password']
      
      # validation => 왜 여기서 처리하려고 하지?
      if password == re_password:
        if len(password >= 8): 
          if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(
              first_name = first_name,
              last_name = last_name,
              username = username,
              password = password,
            )
            user.save()
            
            
      else:
        return Response()
    pass