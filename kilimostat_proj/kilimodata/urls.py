from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
     re_path(r'^api/$', views.data_list),
     re_path(r'^api/([0-9])$', views.data_detail),
    path(f'api/apputils', apputils.as_view(), name="apputils"),
     
   
]