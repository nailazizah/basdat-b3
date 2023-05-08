from django.urls import path
from umpire.views import dashboard_umpire

app_name = 'umpire'

urlpatterns = [
    path('dashboard-umpire/', dashboard_umpire, name='dashboard_umpire' ),
]