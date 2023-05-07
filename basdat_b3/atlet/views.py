from django.shortcuts import render

# Create your views here.

def tes_kualifikasi(request):
    return render(request, "tes_kualifikasi.html")

def tes_kualifikasi_form(request):
    return render(request, "tes_kualifikasi_form.html")
