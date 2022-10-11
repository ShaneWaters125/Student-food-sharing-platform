from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Recipe


# my custom views
def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/home.html', context)


class RecipeListView(ListView):
    model = Recipe
    # template_name and context_object_name is convention in django for templates name and context in class based view
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-dateAdded']


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['recipeName', 'description']


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})
