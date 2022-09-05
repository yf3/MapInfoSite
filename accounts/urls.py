from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views
from .views import FacebookLogin, GoogleLogin

urlpatterns = [
    # path('', include('allauth.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
]
