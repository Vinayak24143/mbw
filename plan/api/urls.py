from django.urls import path

from plan.api.views import PlanFeatureViewSet, PlanViewSet

urlpatterns = [
    path('plans/features', PlanFeatureViewSet.as_view({"get": 'list', 'post': 'create'})),
    path('plans/features', PlanFeatureViewSet.as_view({"get": 'retrieve', 'put':'update', 'delete':'destroy'})),
    path('plans', PlanViewSet.as_view({"get": 'list', 'post': 'create'})),
    path('plans', PlanViewSet.as_view({"get": 'retrieve', 'put':'update', 'delete':'destroy'})),
]
