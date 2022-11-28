from django.urls import path, re_path
from .views import POIView, chatroom, IndexView, TestView, MapPoiTypeList, MapList, MapDetail

urlpatterns = [
    path('map/', MapList.as_view()),
    path('map/<int:pk>/', MapDetail.as_view()),
    path('types/', MapPoiTypeList.as_view()),
    path('poi/', POIView.as_view()),
    #
    path('test/', TestView.as_view()),
    path('', IndexView.as_view()),
    path('chatroom/', chatroom),
]