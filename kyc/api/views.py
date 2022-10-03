from rest_framework import viewsets
from ..models import KYCApplication, KYCDocumentType
from .serializers import KYCApplicationSerializer, KYCDocumentTypeSerializer

class KYCApplicationViewSet(viewsets.ModelViewSet):
    queryset = KYCApplication.objects.all()
    serializer_class = KYCApplicationSerializer

class KYCDocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = KYCDocumentType.objects.all()
    serializer_class = KYCDocumentTypeSerializer