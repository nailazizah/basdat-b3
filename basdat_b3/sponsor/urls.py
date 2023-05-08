from django.urls import path
from .views import *

app_name = "sponsor"

urlpatterns = [
    path("daftar/", sponsor, name="sponsor"),
]