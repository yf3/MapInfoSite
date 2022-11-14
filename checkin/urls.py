from django.urls import path
from .views import POIView, chatroom, IndexView, TestView, POITypeView, MapPoiTypeList

urlpatterns = [
    path('poi/', POIView.as_view()),
    path('poitypes/', POITypeView.as_view()),
    path('map/<int:map_id>/', MapPoiTypeList.as_view()),
    path('test/', TestView.as_view()),
    path('', IndexView.as_view()),
    path('chatroom/', chatroom),
]