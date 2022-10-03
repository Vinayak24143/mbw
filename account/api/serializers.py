from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        # fields = "__all__"
        exclude=['user_permissions','is_staff','is_superuser']
        read_only_fields =['date_joined','last_login','kyc_approved']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields="__all__"