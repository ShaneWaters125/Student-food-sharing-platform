import re

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # fields of UserCreationForm
    email = forms.EmailField(required=True)

    # class with nested namespace for configurations
    class Meta:
        # model interact with form
        model = User
        # field which display in form in order
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The given email is already registered")
        return self.cleaned_data['email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The given email is already registered")
        return self.cleaned_data['email']

    def clean_username(self):
        username = self.cleaned_data['username']
        regex = r'^[\w.@+-]+\Z'
        if not re.search(regex, username):
            raise forms.ValidationError('Provide a valid username')
        return self.cleaned_data['username']
