from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from . import views
from .views import FacebookLogin, GoogleLogin

urlpatterns = [
    # path('', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
]