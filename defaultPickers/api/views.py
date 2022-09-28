from rest_framework import viewsets, exceptions
from .serializers import *
from ..models import *

class CountryViewset(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class StateViewset(viewsets.ModelViewSet):
    queryset=State.objects.all()
    serializer_class=StateSerializer

    def get_queryset(self):
        queryset = State.objects.all()
        country = self.request.query_params.get('country')
    
        if country is not None:
            try:
                country = int(country)
            except ValueError:
                raise exceptions.ValidationError("country query perameter must be an integers")
            except:
                pass

            queryset = queryset.filter(country__id =country)
        return queryset

class DistrictViewset(viewsets.ModelViewSet):
    queryset=District.objects.all()
    serializer_class=DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        state = self.request.query_params.get('state')
    
        if state is not None:
            try:
                state = int(state)
            except ValueError:
                raise exceptions.ValidationError("state query perameter must be an integers")
            except:
                pass

            queryset = queryset.filter(state__id =state)
        return queryset

class CityViewset(viewsets.ModelViewSet):
    queryset=City.objects.all()
    serializer_class=CitySerializer

    def get_queryset(self):
        queryset = District.objects.all()
        state = self.request.query_params.get('state')
        district = self.request.query_params.get('district')
    
        if state is not None:
            try:
                state = int(state)
            except ValueError:
                raise exceptions.ValidationError("state query perameter must be an integers")
            except:
                pass

            queryset = queryset.filter(state__id =state)

        if district is not None:
            try:
                district = int(district)
            except ValueError:
                raise exceptions.ValidationError("district query perameter must be an integers")
            except:
                pass

            queryset = queryset.filter(district__id =district)
        return queryset