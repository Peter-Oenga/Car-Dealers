from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def description(request):
    return render(request, "description.html")