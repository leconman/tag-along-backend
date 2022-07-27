from django.shortcuts import render
from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from .forms import UserForm

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

def home_view(request):
    context = {}
    context['form'] = UserForm()
    return render(request, context)
