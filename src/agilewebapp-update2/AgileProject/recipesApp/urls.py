from django.urls import path
from . import views

# urls for recipes app
urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('about/', views.about, name='recipes-about')
]
