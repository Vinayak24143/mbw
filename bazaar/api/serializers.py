from bazaar.models import Bazaar
from rest_framework import serializers

class BazaarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bazaar
        fields = "__all__"