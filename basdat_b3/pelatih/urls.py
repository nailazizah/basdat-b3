from django.urls import path
from pelatih.views import dashboard_pelatih

app_name = 'pelatih'

urlpatterns = [
    path('dashboard-pelatih/', dashboard_pelatih, name='dashboard_pelatih' ),
]