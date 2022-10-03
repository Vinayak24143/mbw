from pyexpat import model
from ..models import KYCApplication,KYCDocument,KYCDocumentType

from rest_framework import serializers

class KYCApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=KYCApplication
        fields='__all__'

class KYCDocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=KYCDocumentType
        fields="__all__"