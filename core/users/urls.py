
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.UserDetail.as_view(), name="customuser-detail"),
    path('', views.UserList.as_view()),
]
