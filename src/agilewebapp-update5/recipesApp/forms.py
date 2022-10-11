from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.forms import modelformset_factory

from .models import Recipe, Ingredient, Nutrient


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = [
            'recipeName', 'description', 'instruction', 'recipeCategory', 'cost', 'cookingTime', 'portion',
            'skillsLevel', 'image'
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['recipeName', 'ingredient']
        exclude = ['recipeName']


class NutrientForm(forms.ModelForm):
    class Meta:
        model = Nutrient
        fields = ['recipeName', 'calories', 'fat', 'carbohydrate', 'fibre', 'protein', 'salt']
        exclude = ['recipeName']


IngredientInlineFormset = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    min_num=3,
    extra=0,
    can_delete=False
)

# NutrientInlineFormset = inlineformset_factory(
#     Recipe,
#     Nutrient,
#     form=NutrientForm,
#     can_delete=False
# )
