from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm


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
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'users/profile.html', context)
