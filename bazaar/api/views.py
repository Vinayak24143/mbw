from rest_framework import viewsets
from bazaar.models import *
from .serializers import *

class BazaarViewSet(viewsets.ModelViewSet):
    queryset = Bazaar.objects.all()
    serializer_class = BazaarSerializer

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