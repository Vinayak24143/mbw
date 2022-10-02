from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from ..models import*

class PlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanFeature
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields = "__all__"