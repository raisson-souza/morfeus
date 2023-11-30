from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def morfeus(request):
    return render(request, "morfeus.html")
