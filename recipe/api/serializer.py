from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from recipe.models import Recipe, Step, Ingredient

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('step_text', 'recipe')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('text', 'recipe')                

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =('username','email', 'first_name','last_name')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('name', 'user')

