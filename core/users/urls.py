
from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import *
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register(r'users', CustomUserList, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', views.UserDetail.as_view(), name="customuser-detail"),
    path('', views.UserList.as_view()),
]
