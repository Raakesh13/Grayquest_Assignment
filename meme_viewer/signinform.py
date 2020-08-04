from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    # def clean_message(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     user = authenticate(username=username, password=password)
    #     print(username)
    #     print(password)

    #     # if user is not None:
    #     # # A backend authenticated the credentials
    #     # else:
    #     # # No backend authenticated the credentials
    #     # dbuser = Dreamreal.objects.filter(name=username)
    #     print(user)
    #     if not user:
    #         raise forms.ValidationError("User does not exist in our db!")
    #     return username
