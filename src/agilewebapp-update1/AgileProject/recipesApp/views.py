from django.shortcuts import render
from django.http import HttpResponse

from .forms import RecipeForm
from .models import Recipe


# my custom views
def home(request):
    context = {

    }
    return render(request, 'recipes/home.html', context)


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})


#####
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RecipeForm()
    context = {
        'form': form
    }
    return render(request, "recipes/recipe_create.html", context)


def recipe_detail_view(request):
    obj = Recipe.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "recipes/recipe_detail.html", context)
