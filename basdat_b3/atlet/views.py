from django.shortcuts import render

# Create your views here.


def daftar_event(request):
    return render(request, "daftar_event.html")

def event_stadium(request):
    return render(request, "event_stadium.html")

def event_kategori(request):
    return render(request, "event_kategori.html")

def enrolled_event(request):
    return render(request, "enrolled_event.html")
    
def tes_kualifikasi(request):
    return render(request, "tes_kualifikasi.html")

def tes_kualifikasi_form(request):
    return render(request, "tes_kualifikasi_form.html")

def dashboard_atlet(request):
    return render(request, "dashboard_atlet.html")