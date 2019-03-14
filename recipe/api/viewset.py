from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from recipe.models import Recipe, Step, Ingredient
from .serializer import UserSerializer, RecipeSerializer, StepSerializer, IngredientSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

def perform_destroy(self, Recipe):
    Recipe.delete()
def perform_update(self, RecipeSerializer):
    RecipeSerializer.save()

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer        