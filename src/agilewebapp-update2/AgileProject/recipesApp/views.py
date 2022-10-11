from django.shortcuts import render

from .forms import RecipeForm
from .models import Recipe


# my custom views
def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/home.html', context)


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})