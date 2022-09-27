from django.urls import path, include
from .views import *
urlpatterns = [
   path('bazaars', BazaarViewSet.as_view({'get':'list','post':'create'})),
   path('bazaars/<int:pk>', BazaarViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products', ProductViewSet.as_view({'get':'list','post':'create'})),
   path('products/<int:pk>', ProductViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products/categories', ProductCategoryViewSet.as_view({'get':'list','post':'create'})),
   path('products/categories/<int:pk>', ProductCategoryViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('products/subcategories', ProductSubCategoryViewSet.as_view({'get':'list','post':'create'})),
   path('products/subcategories/<int:pk>', ProductSubCategoryViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
   path('bazaars/groups', BazaarGroupCategoryViewSet .as_view({'get':'list','post':'create'})),
   path('bazaars/groups/<int:pk>', BazaarGroupCategoryViewSet .as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
]