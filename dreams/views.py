from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dreams import forms, models
from django.contrib import messages

def home(request):
    return render(request, "home.html")

@login_required
def morfeus(request):
    my_dreams_count = models.Dream.objects.filter(author_id=request.user.id).count()
    total_dreams_count = models.Dream.objects.count()
    users_count = models.User.objects.count()

    dreams_type_count = models.Dream.objects.filter(dream_type="SONHO").count()
    nightmares_type_count = models.Dream.objects.filter(dream_type="PESADELO").count()

    my_dreams_type_count = models.Dream.objects.filter(dream_type="SONHO", author_id=request.user.id).count()
    my_nightmares_type_count = models.Dream.objects.filter(dream_type="PESADELO", author_id=request.user.id).count()

    # MY_DREAMS_COUNT
    if my_dreams_count == 0:
        my_dreams_count = "Nenhum sonho cadastrado por mim."
    else:
        my_dreams_count = f"{ my_dreams_count } { 'sonhos' if my_dreams_count > 1 else 'sonho' } { 'cadastrados' if my_dreams_count > 1 else 'cadastrado' } por mim."

    # TOTAL_DREAMS_COUNT
    if total_dreams_count == 0:
        total_dreams_count = "Nenhum sonho cadastrado no sistema."
    else:
        total_dreams_count = f"{ total_dreams_count } { 'sonhos' if total_dreams_count > 1 else 'sonho' } { 'cadastrados' if total_dreams_count > 1 else 'cadastrado' } no sistema."

    # USERS_COUNT
    users_count = f"{ users_count } { 'usuários' if users_count > 1 else 'usuário' } { 'cadastrados' if users_count > 1 else 'cadastrado' } no sistema."

    return render(request, "morfeus.html", {
        'my_dreams_count': my_dreams_count,
        'total_dreams_count': total_dreams_count,
        'users_count': users_count,
        'dreams_type_count': dreams_type_count,
        'my_dreams_type_count': my_dreams_type_count,
        'nightmares_type_count': nightmares_type_count,
        'my_nightmares_type_count': my_nightmares_type_count
    })

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