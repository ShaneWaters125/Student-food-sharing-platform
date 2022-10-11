from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def recipe_view(request, *args, **kwargs):
    return render(request, "recipes.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is contact to us',
        'my_number': 123,
        'my_list': [1245, 43, 66, 'aBc',234]
    }
    return render(request, "contact.html", my_context)
