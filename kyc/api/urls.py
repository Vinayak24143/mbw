from django.urls import path
from .views import KYCApplicationViewSet,KYCDocumentTypeViewSet

urlpatterns=[
    path("kyc/applications",KYCApplicationViewSet.as_view({"get":"list",'post':'create'})),
    path("kyc/applications/<pk>",KYCApplicationViewSet.as_view({"get":"retrieve",'put':'update','delete':'destroy'})),
    path("kyc/doc/types",KYCDocumentTypeViewSet.as_view({"get":"list",'post':'create'})),
    path("kyc/doc/types/<pk>",KYCApplicationViewSet.as_view({"get":"retrieve",'put':'update','delete':'destroy'})),
]