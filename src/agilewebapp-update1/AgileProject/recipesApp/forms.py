from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'recipeName',
            'cost',
            'portion',
            'description',
            'guide',
            'cookingTime',
            'skillsLevel'
        ]
