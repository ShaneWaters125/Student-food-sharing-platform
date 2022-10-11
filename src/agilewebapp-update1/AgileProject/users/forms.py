from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # fields of UserCreationForm
    email = forms.EmailField()

    # class with nested namespace for configurations
    class Meta:
        # model interact with form
        model = User
        # field which display in form in order
        fields = ['username', 'email', 'password1', 'password2']