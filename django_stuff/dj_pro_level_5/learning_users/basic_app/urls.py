from django.urls import url, path
from basic_app import views

# Template URLs
app_name = 'basic_app'

urlpatterns = [
    url(r'register', views.register, name='register')
]