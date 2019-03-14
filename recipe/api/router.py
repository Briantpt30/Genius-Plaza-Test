from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from .viewset import UserViewSet, RecipeViewSet , IngredientViewSet, StepViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'steps', StepViewSet)
