from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dreams import forms, models
from django.contrib import messages

def home(request):
    return render(request, "home.html")

@login_required
def morfeus(request):
    return render(request, "morfeus.html")

@login_required
def create_dream(request):
    if request.method == 'GET':
        form = forms.DreamRegister()
        return render(request, 'create_dream.html', { 'form' : form })
    
    if request.method == 'POST':
        form = forms.DreamRegister(request.POST)

        if form.is_valid():
            dream = models.Dream()
            dream.author = request.user
            dream.title = form.cleaned_data["title"]
            dream.text = form.cleaned_data["text"]
            dream.dream_type = form.cleaned_data["dream_type"]
            dream.date = form.cleaned_data["date"]

            dream.save()
            return redirect(dreams)
        
        messages.error(request, "Data do sonho inválida.")
        return render(request, 'create_dream.html', { 'form' : form })

@login_required
def dreams(request):
    dreams = models.Dream.objects.filter(author_id=request.user.id).order_by("-date")
    return render(request, "dreams.html", { 'dreams': dreams })