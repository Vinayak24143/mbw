from rest_framework import viewsets
from bazaar.models import Bazaar
from .serializers import BazaarSerializer

class BazaarViewSet(viewsets.ModelViewSet):
    queryset = Bazaar.objects.all()
    serializer_class = BazaarSerializer