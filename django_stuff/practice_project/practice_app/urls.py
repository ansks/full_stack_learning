from django.urls import path
from practice_app import views

urlpatterns = [
    # path('', views.help, name = 'help'),
    path('', views.user_list, name = 'userinfo'),
]