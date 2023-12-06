from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dreams import forms, models
from django.contrib import messages

def home(request):
    return render(request, "home.html")

@login_required
def morfeus(request):
    def render_phrase(value : int, phrase : str):
        return f"{ value } sonhos { phrase }." if value == 0 or value > 1 else f"{ value } sonho { phrase }."

    my_dreams_count = models.Dream.objects.filter(author_id=request.user.id).count()
    total_dreams_count = models.Dream.objects.count()
    users_count = models.User.objects.count()

    ok_feeling = models.Dream.objects.filter(author_id=request.user.id, feeling__in=["Normal","Feliz"]).count()
    ok_feeling = render_phrase(ok_feeling, "se sentindo bem")
    not_ok_feeling = models.Dream.objects.filter(author_id=request.user.id, feeling__in=["Triste","Raivoso","Assustado"]).count()
    not_ok_feeling = render_phrase(not_ok_feeling, "se sentindo mal")

    partially_lucid_dreams = models.Dream.objects.filter(author_id=request.user.id, lucid__in=["Não Lúcido", "Parcialmente Lúcido"]).count()
    partially_lucid_dreams = render_phrase(partially_lucid_dreams, "enquanto parcialmente lúcido ou não")
    lucid_dreams = models.Dream.objects.filter(author_id=request.user.id, lucid="Lúcido").count()
    lucid_dreams = render_phrase(lucid_dreams, "lúcidos")

    day_dreams = models.Dream.objects.filter(author_id=request.user.id, period="Dia").count()
    day_dreams = render_phrase(day_dreams, "de dia")
    night_dreams = models.Dream.objects.filter(author_id=request.user.id, period="Noite").count()
    night_dreams = render_phrase(night_dreams, "de noite")

    dreams_type_count = models.Dream.objects.filter(dream_type="Sonho").count()
    nightmares_type_count = models.Dream.objects.filter(dream_type="Pesadelo").count()

    my_dreams_type_count = models.Dream.objects.filter(dream_type="Sonho", author_id=request.user.id).count()
    my_nightmares_type_count = models.Dream.objects.filter(dream_type="Pesadelo", author_id=request.user.id).count()

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
        'my_nightmares_type_count': my_nightmares_type_count,
        'ok_feeling': ok_feeling,
        'not_ok_feeling': not_ok_feeling,
        'partially_lucid_dreams': partially_lucid_dreams,
        'lucid_dreams': lucid_dreams,
        'day_dreams': day_dreams,
        'night_dreams': night_dreams
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
            dream.feeling = form.cleaned_data["feeling"]
            dream.lucid = form.cleaned_data["lucid"]
            dream.period = form.cleaned_data["period"]
            dream.date = form.cleaned_data["date"]
            dream.public = form.cleaned_data["public"]

            dream.save()
            return redirect(dreams)
        
        messages.error(request, "Data do sonho inválida.")
        return render(request, 'create_dream.html', { 'form' : form })

@login_required
def dreams(request):
    dreams = models.Dream.objects.filter(author_id=request.user.id).order_by("-date")

    for dream in dreams:
        dream.text = dream.text[:150]

    return render(request, "dreams.html", { 'dreams': dreams })

@login_required
def public_dreams(request):
    dreams = models.Dream.objects.filter(public=True).order_by("-date")

    for dream in dreams:
        dream.title = dream.title[:30] + "..." if len(dream.title) > 30 else dream.title
        dream.text = dream.text[:150] + "..." if len(dream.text) > 150 else dream.text

    return render(request, "public_dreams.html", { 'dreams': dreams })
