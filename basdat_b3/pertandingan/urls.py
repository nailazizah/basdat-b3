from django.urls import path
from .views import show_pertandingan, show_hasil_pertandingan

app_name = "pertandingan"

urlpatterns = [
    path('', show_pertandingan, name="show_pertandingan"),
    path('hasil/', show_hasil_pertandingan, name="show_hasil_pertandingan"),
]