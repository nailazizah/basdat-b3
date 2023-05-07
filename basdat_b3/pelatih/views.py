from django.shortcuts import render

# Create your views here.

def dashboard_pelatih(request):
    return render(request, "dashboard_pelatih.html")

