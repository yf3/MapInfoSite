from decouple import config

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import POI, POIType, Map
from .serializers import POISerializer, UserSerializer, POITypeSerializer, MapSerializer

class MapList(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        query_set = Map.objects.all()
        serializer = MapSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MapDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_item(self, pk):
        try:
            return Map.objects.get(id=pk)
        except Map.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = MapSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MapPoiTypeList(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request, map_id, format=None):
        query_set = POIType.objects.filter(map_id=map_id)
        serializer = POITypeSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class POIView(APIView):
    parser_classes = [MultiPartParser,]
    renderer_classes = [JSONRenderer]

    def get(self, request, map_id, format=None):
        query_set = POI.objects.filter(map_id=map_id)
        serializer = POISerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = POISerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def chatroom(request):
    return render(request, template_name='chatroom.html')

class IndexView(TemplateView):
    extra_context = {'google_map_key': config('GOOGLE_MAP_KEY')}
    template_name = 'index.html'

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
