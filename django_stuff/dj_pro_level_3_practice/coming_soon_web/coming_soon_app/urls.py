from django.urls import path
from coming_soon_app import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'', views.thank_you, name='thankyou'),
    path(r'', views.user_signup, name='signup'),
    ]