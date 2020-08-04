from rest_framework import authentication
from xyo.models import Agency, Personnel
from .serializers import AgencySerializer, PersonnelSerializer
from rest_framework import viewsets


class AgencyViewSet(viewsets.ModelViewSet):
    serializer_class = AgencySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Agency.objects.all()


class PersonnelViewSet(viewsets.ModelViewSet):
    serializer_class = PersonnelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Personnel.objects.all()
