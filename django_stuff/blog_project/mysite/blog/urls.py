from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('about', views.AboutView.as_view(), name = 'about'),
]
