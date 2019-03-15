from rest_framework import viewsets, generics, status
from recipe.models import Recipe, Step, Ingredient
from .serializer import UserSerializer, RecipeSerializer, StepSerializer, IngredientSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.select_related()


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@api_view(['GET'])
def user_recipe(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    if request.method == 'GET':
        recipe = Recipe.objects.all().filter(user=pk)
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)