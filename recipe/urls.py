from django.urls import path
from recipe.api.viewset import user_recipe

urlpatterns = [
    path('<int:pk>', user_recipe, name='user-recipe')
]