from rest_framework import serializers
from .models import POI, POIType, Attribute
from django.contrib.auth.models import User

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = "__all__"

class POITypeSerializer(serializers.ModelSerializer):
    # pois = serializers.PrimaryKeyRelatedField(queryset=POI.objects.all(), many=True, read_only=False)
    # attributes = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all(), many=True, read_only=False)
    class Meta:
        model = POIType
        fields = "__all__"

    def create(self, validated_data):
        return POIType(validated_data)

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']