from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
    paginate_by = 2


class UserRecipeListView(ListView):
    model = Recipe
    # template_name and context_object_name is convention in django for templates name and context in class based view
    template_name = 'recipes/user_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipe.objects.filter(author=user).order_by('-dateAdded')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['recipeName', 'description', 'guide', 'recipeCategory', 'cost', 'cookingTime', 'portion', 'skillsLevel',
              'dateAdded', 'image']

    # override form_valid method setting the author on the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['recipeName', 'description', 'guide', 'recipeCategory', 'cost', 'cookingTime', 'portion', 'skillsLevel',
              'dateAdded', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function check if user pass test condition - if user is an author of updated post
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})
