from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AgencyViewSet, PersonnelViewSet

router = DefaultRouter()
router.register("agency", AgencyViewSet)
router.register("personnel", PersonnelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
