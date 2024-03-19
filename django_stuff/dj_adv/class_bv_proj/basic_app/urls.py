from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListview.as_view(), 
         name = 'list_view'),  # name is coming from nav view defined in basic_app_base.html
    re_path(r'^(?P<pk>\d+)/',
            view=views.SchoolDetailView.as_view(), 
            name = 'detail'),
    re_path(r'^create/$', views.SchoolCreateView.as_view(),
            name = 'create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(),
            name = 'update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(),
            name = 'delete')
]
