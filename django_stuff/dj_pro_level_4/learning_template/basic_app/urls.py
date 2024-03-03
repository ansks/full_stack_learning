from django.urls import path, include
# from django.conf.urls import url

from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path(r'relative/', views.relative, name='relative'),
    path(r'other/', views.other, name='other'),
]