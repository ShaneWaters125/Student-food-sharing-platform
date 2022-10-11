from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView
)
from . import views

# urls for css app
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes-home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('about/', views.about, name='recipes-about')
]
