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