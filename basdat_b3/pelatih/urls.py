
from django.conf.urls import include
from django.urls import path
from pelatih.views import *

app_name = 'pelatih'

urlpatterns = [
    path('daftar-atlet/', daftar_atlet, name='daftar_atlet'),
    path('list-atlet/', list_atlet, name='list_atlet'),
    path('dashboard-pelatih/', dashboard_pelatih, name='dashboard_pelatih' ),
]