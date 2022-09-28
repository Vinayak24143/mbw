from rest_framework import viewsets, exceptions
from bazaar.models import *
from .serializers import *
import json


class BazaarViewSet(viewsets.ModelViewSet):
    queryset = Bazaar.objects.all()
    serializer_class = BazaarSerializer

    def get_queryset(self):
        queryset = Bazaar.objects.all()
        states = self.request.query_params.get('states')
        districts = self.request.query_params.get('districts')
        cities = self.request.query_params.get('cities')

        if states is not None:
            try:
                states = json.loads(states)
                if type(states) is not list:
                    raise exceptions.ValidationError("states query perameter must be a list of integers")
            except json.decoder.JSONDecodeError:
                raise exceptions.ValidationError("states query perameter must be a list of integers")
            except:
                pass

            queryset = queryset.filter(state__id__in=states)

        if districts is not None:
            try:
                districts = json.loads(districts)
                if type(districts) is not list:
                    raise exceptions.ValidationError("districts query perameter must be a list of integers")
            except json.decoder.JSONDecodeError:
                raise exceptions.ValidationError("districts query perameter must be a list of integers")
            except:
                pass

            queryset = queryset.filter(dist__id__in=districts)
        
        if cities is not None:
            try:
                cities = json.loads(cities)
                if type(cities) is not list:
                    raise exceptions.ValidationError("cities query perameter must be a list of integers")
            except json.decoder.JSONDecodeError:
                raise exceptions.ValidationError("cities query perameter must be a list of integers")
            except:
                pass

            queryset = queryset.filter(city__id__in=cities)
        return queryset

class BazaarGroupCategoryViewSet(viewsets.ModelViewSet):
    queryset = GroupCategory.objects.all()
    serializer_class = BazaarGroupCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer