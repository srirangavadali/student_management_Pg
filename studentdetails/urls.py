from django.urls import path
from . import views

urlpatterns = [
 path('', views.homepage, name='home'),
path('rec_data', views.rec_data, name='rec_data'),
    path('index', views.index, name='index'),


]
