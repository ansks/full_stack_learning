from django.urls import path
from app_level_2 import views

urlpatterns = [
    path(r'', views.users, name='users'),
    ]