from typing import ValuesView
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User=get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset = User.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer