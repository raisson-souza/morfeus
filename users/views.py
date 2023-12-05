from django.shortcuts import render, redirect
from users import forms
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django, logout
from dreams.views import morfeus

def login(request):
    errors = []

    if request.method == 'POST':
        form = forms.UsersLogin(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.get(email=email)

            if user is not None:
                if user.check_password(password):
                    login_django(request, user)
                    return redirect(morfeus)
                
                else:
                    errors.append("senha incorreta.")

            else:
                errors.append("email não encontrado.")
        else:
            return render(request, 'login.html', { 'form' : form, 'errors' : form.errors })
        # PROBLEMA NO LOGIN AO DIGITAR EMAIL ERRADO

    form = forms.UsersLogin(request.POST)
    return render(request, 'login.html', { 'form' : form, 'errors' : errors })


def register(request):
    if request.method == 'GET':
        form = forms.UsersRegister()
        return render(request, 'register.html', { 'form' : form })
    
    if request.method == 'POST':
        form = forms.UsersRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')

def logoff(request):
    logout(request)
    return redirect('home')
