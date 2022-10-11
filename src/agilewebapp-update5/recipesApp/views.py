import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connection
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from formtools.wizard.views import SessionWizardView, WizardView
from django.core.files.storage import FileSystemStorage
from .forms import *

logger = logging.getLogger('django')


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

    paginate_by = 9

    def get_queryset(self):
        category = self.request.GET.get('c','NONE')
        search = self.request.GET.get('s', 'NONE')
        if category != 'NONE':
            return Recipe.objects.filter(recipeCategory=category).order_by('-dateAdded')
        if search != 'NONE':
            return Recipe.objects.filter(recipeName__icontains=search).order_by('-dateAdded')
        return Recipe.objects.all().order_by('-dateAdded')



class MyRecipeView(ListView):
    model = Recipe
    # template_name and context_object_name is convention in django for templates name and context in class based view
    template_name = 'recipes/my_recipe.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self):
        self.kwargs = {"username": self.request.user.username}
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        logger.info('url:%s method:%s ' % (self.request.path, self.request.method))
        return Recipe.objects.filter(author=user).order_by('-dateAdded')


class UserRecipeListView(ListView):
    model = Recipe
    # template_name and context_object_name is convention in django for templates name and context in class based view
    template_name = 'recipes/user_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        logger.info('url:%s method:%s ' % (self.request.path, self.request.method))
        return Recipe.objects.filter(author=user).order_by('-dateAdded')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class FormWizardView(LoginRequiredMixin, SessionWizardView):
    template_name = "recipes/recipe_form.html"
    form_list = [RecipeForm, IngredientInlineFormset, NutrientForm]
    file_storage = FileSystemStorage(location='/mediafiles/recipes_pics')

    def done(self, form_list, **kwargs):
        form_list[0].instance.author = self.request.user
        recipeID = (form_list[0].save().id)
        for form in form_list[1]:
            form.instance.recipeName_id = recipeID
            form.save()
        form_list[2].instance.recipeName_id = recipeID
        form_list[2].save()

        logger.info('url:%s method:%s ' % (self.request.path, self.request.method))
        return redirect(reverse_lazy("recipe-detail", kwargs={'pk': recipeID}))


class UpdateFormWizardView(LoginRequiredMixin, SessionWizardView):
    template_name = "recipes/recipe_form.html"
    file_storage = FileSystemStorage(location='/mediafiles/recipes_pics')

    def get_form_initial(self, step):
        if 'pk' in self.kwargs:
            return {}
        return self.initial_dict.get(step, {})

    def get_form_instance(self, step):
        if not self.instance_dict:
            if 'pk' in self.kwargs and step == 'RecipeForm':
                pk = self.kwargs['pk']
                # print(Nutrient.objects.all())
                return Recipe.objects.get(id=pk)
            elif 'pk' in self.kwargs and step == '1':
                pk = self.kwargs['pk']
                result = Recipe.objects.get(id=pk)
                return result
            elif 'pk' in self.kwargs and step == 'NutrientForm':
                pk = self.kwargs['pk']
                print(Nutrient.objects.get(recipeName=pk))
                return Nutrient.objects.get(recipeName=pk)
        return self.initial_dict.get(step, None)

    def done(self, form_list, **kwargs):
        form_list[0].instance.author = self.request.user
        recipeID = (form_list[0].save().id)
        for form in form_list[1]:
            form.instance.recipeName_id = recipeID
            # print(form)
            form.save()
        form_list[2].instance.recipeName_id = recipeID
        form_list[2].save()

        logger.info('url:%s method:%s ' % (self.request.path, self.request.method))
        return redirect(reverse_lazy("recipe-detail", kwargs={'pk': recipeID}))


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_message = "This recipe was deleted successfully"

    def get_success_url(self):
        messages.success(self.request, "The recipe was deleted successfully")
        return reverse('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        logger.info('url:%s method:%s ' % (self.request.path, self.request.method))
        if self.request.user == recipe.author:
            return True
        return False


def about(request):
    logger.info('url:%s method:%s ' % (request.path, request.method))
    return render(request, 'recipes/about.html', {'title': 'About'})
