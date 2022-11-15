from rest_framework import serializers
from .models import POI, POIType, Map
from django.contrib.auth.models import User

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"
        
class POISerializer(serializers.ModelSerializer):
    map_id = serializers.PrimaryKeyRelatedField(queryset=Map.objects.all())
    poi_type = serializers.PrimaryKeyRelatedField(allow_null=True, required=False, queryset=POIType.objects.all())

    class Meta:
        model = POI
        fields = "__all__"

    def validate(self, attrs):
        valid_types = POIType.objects.filter(map_id=attrs['map_id'])
        if valid_types.filter(id=attrs['poi_type'].id).exists():
            return attrs
        else:
            raise serializers.ValidationError()
            # TODO: error message

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
