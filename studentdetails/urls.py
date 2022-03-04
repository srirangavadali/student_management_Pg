from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('rec_data', views.rec_data, name='rec_data'),
    path('index', views.index, name='index'),
    #path('table_data',views.table_data, name='table_data')
    path('table_data', views.table_data, name='table_data'),


]
