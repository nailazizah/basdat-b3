
from django.conf.urls import include
from atlet.views import *
from django.urls import path
from atlet.views import *

app_name = 'atlet'

urlpatterns = [
    path('daftar-event/stadium/', event_stadium, name='event_stadium'),
    path('daftar-event/stadium/event/', daftar_event, name='daftar_event'),
    path('daftar-event/stadium/event/kategori', event_kategori, name='event_kategori' ),
    path('enrolled-event/', enrolled_event, name='enrolled_event'),
    path('tes-kualifikasi-form/', tes_kualifikasi_form, name='tes_kualifikasi_form' ),
    path('tes-kualifikasi/', tes_kualifikasi, name='tes_kualifikasi' ),
    path('dashboard-atlet/', dashboard_atlet, name='dashboard_atlet' ),
]