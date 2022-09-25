from rest_framework import viewsets
from .serializers import *
from ..models import *

class CountryViewset(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class StateViewset(viewsets.ModelViewSet):
    queryset=State.objects.all()
    serializer_class=StateSerializer

class DistrictViewset(viewsets.ModelViewSet):
    queryset=District.objects.all()
    serializer_class=DistrictSerializer

class CityViewset(viewsets.ModelViewSet):
    queryset=City.objects.all()
    serializer_class=CitySerializer
