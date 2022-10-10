from django.urls import path
from .views import POIView, chatroom, IndexView, TestView, POITypeView

urlpatterns = [
    path('poi/', POIView.as_view()),
    path('poitype/', POITypeView.as_view()),
    path('test/', TestView.as_view()),
    path('', IndexView.as_view()),
    path('chatroom/', chatroom),
]