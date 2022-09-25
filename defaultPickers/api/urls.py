from django.urls import path
from .views import *

urlpatterns=[
    path('countries', CountryViewset.as_view({'get':'list','post':'create'})),
    path('countries/<pk>', CountryViewset.as_view({'put':'update','get':'retrieve','delete':'destroy'})),
    path('states', StateViewset.as_view({'get':'list','post':'create'})),
    path('districts', DistrictViewset.as_view({'get':'list','post':'create'})),
    path('cities', CityViewset.as_view({'get':'list','post':'create'})),
]