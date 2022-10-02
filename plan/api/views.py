from rest_framework import viewsets

from plan.api.serializers import PlanFeatureSerializer, PlanSerializer
from ..models import PlanFeature, Plan
from django_filters.rest_framework import DjangoFilterBackend

class PlanFeatureViewSet(viewsets.ModelViewSet):
    queryset = PlanFeature.objects.all()
    serializer_class = PlanFeatureSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bazaars', 'states', 'districts','cities','amount','is_active']
