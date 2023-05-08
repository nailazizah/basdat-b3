from django.shortcuts import render

# Create your views here.

def dashboard_umpire(request):
    return render(request, "dashboard_umpire.html")


