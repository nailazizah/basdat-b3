from django.shortcuts import render

# Create your views here.
def sponsor(request):
    return render(request, "sponsor.html")