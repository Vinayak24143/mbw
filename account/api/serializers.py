from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["id", "first_name", "last_name", "email","mobile", 'groups',"user_permissions","is_active"]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields="__all__"