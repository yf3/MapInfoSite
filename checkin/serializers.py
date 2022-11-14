from rest_framework import serializers
from .models import POI, POIType
from django.contrib.auth.models import User

class POISerializer(serializers.ModelSerializer):
    # poi_type = serializers.PrimaryKeyRelatedField(allow_null=True, required=False, queryset=POIType.objects.all())

    class Meta:
        model = POI
        fields = "__all__"

class POITypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = POIType
        fields = "__all__"

    def create(self, validated_data):
        return POIType(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
