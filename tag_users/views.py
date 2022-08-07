from django.shortcuts import render
from .models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all(),
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MatchedUsers(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, pk):
        user = User.objects.get(pk = pk)
        user.findCluster()
        user.save()
        matches = User.objects.filter(MatchCluster = user.MatchCluster, Location = user.Location)
        
        matchedUsers = [match.Username for match in matches if user.Username != match.Username]
        return Response(matchedUsers)
        


