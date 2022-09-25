from django.urls import path, include
from .views import BazaarViewSet
urlpatterns = [
   path('', BazaarViewSet.as_view({'get':'list'}))
]