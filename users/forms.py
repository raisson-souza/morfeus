from django import forms

class UsersRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UsersLogin(forms.Form):
    email = forms.EmailField(label="Insira o e-mail")
    password = forms.CharField(widget=forms.PasswordInput)
