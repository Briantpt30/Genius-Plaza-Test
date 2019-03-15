from django.contrib.auth.models import User
from rest_framework import serializers
from recipe.models import Recipe, Step, Ingredient


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('step_text', 'recipe')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('text', 'recipe', 'user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('name', 'user', 'ingredients', 'steps')
