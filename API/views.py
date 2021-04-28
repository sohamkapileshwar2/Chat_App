from django.shortcuts import render

from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from Main.models import *

from API.serializers import *

# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
