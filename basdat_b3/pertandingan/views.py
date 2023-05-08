from django.shortcuts import render

# Create your views here.
def show_pertandingan(request):
    return render(request, "pertandingan.html")

def show_hasil_pertandingan(request):
    return render(request, "hasilPertandingan.html")