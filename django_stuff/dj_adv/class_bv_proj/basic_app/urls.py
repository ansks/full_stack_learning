from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListview.as_view(), name = 'list_view'),  # name is coming from nav view defined in basic_app_base.html
    re_path(r'^(?P<pk>[-\w]+)/$', view=views.SchoolDetailView.as_view(), name = 'detail')
]
