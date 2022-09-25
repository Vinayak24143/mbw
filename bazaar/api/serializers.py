from bazaar.models import Bazaar, Product, ProductCategory, ProductSubCategory, Group
from rest_framework import serializers

class BazaarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bazaar
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = "__all__"

class BazaarGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"