from django.urls import path, include
from .views import *
urlpatterns = [
   path('groups', GroupViewSet.as_view({'get':'list','post':'create'})),
   path('permissions', PermissionViewSet.as_view({'get':'list','post':'create'})),
   path('users', UserViewset.as_view({'get':'list','post':'create'})),
]