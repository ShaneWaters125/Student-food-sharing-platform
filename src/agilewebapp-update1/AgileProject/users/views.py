from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    # post request contains user post request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # check that user creation form is valid from post request
        if form.is_valid():
            # save user form with hashed password
            form.save()
            username = form.cleaned_data.get('username')
            # flash message shows received valid data - one-time alert
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
