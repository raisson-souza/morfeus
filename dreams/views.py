from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def morfeus(request):
    return render(request, "morfeus.html")

@login_required
def dreams(request):
    return render(request, "dreams.html")
