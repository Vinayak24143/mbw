from django.urls import path, include
from .views import *
urlpatterns = [
   path('bazaars', BazaarViewSet.as_view({'get':'list','post':'create'})),
   path('bazaars/<pk>', BazaarViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products', ProductViewSet.as_view({'get':'list','post':'create'})),
   path('products/<pk>', ProductViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products/categories', ProductCategoryViewSet.as_view({'get':'list','post':'create'})),
   path('products/categories/<pk>', ProductCategoryViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products/subcategories', ProductSubCategoryViewSet.as_view({'get':'list','post':'create'})),
   path('products/subcategories/<pk>', ProductSubCategoryViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('bazaars/groups', BazaarGroupViewSet .as_view({'get':'list','post':'create'})),
   path('bazaars/groups/<pk>', BazaarGroupViewSet .as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
]