from django.urls import path
from users import views as user_views

# urls for css app
urlpatterns = [
    path('delete-account/', user_views.delAccount, name='deleteAccount'),
]
