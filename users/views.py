from django.shortcuts import render, redirect
from users import forms
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django

def login(request):
    errors = []

    # if request.method == 'GET':
    #     form = forms.UsersLogin()
    #     return render(request, 'login.html', { 'form' : form })
    
    if request.method == 'POST':
        form = forms.UsersLogin(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.get(email=email)

            if user is not None:
                if user.check_password(password):
                    login_django(request, user)
                    return render(request, 'index.html')
                
                else:
                    errors.append("senha incorreta.")

            else:
                errors.append("email não encontrado.")
            
    form = forms.UsersLogin()
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
            return redirect(login)

# Create your views here.
