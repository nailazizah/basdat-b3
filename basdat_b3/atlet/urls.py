from django.urls import path
from atlet.views import tes_kualifikasi, tes_kualifikasi_form

app_name = 'atlet'

urlpatterns = [
    path('tes-kualifikasi-form/', tes_kualifikasi_form, name='tes_kualifikasi_form' ),
    path('tes-kualifikasi/', tes_kualifikasi, name='tes_kualifikasi' ),
]