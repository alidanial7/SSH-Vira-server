from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'user/', include('users.urls')),
    url(r'base/', include('base.urls')),
    url(r'kitchen/', include('kitchen.urls')),
    path('auth/', include('users.urls')),
]
