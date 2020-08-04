from rest_framework import serializers
from xyo.models import Agency, Personnel


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__"
