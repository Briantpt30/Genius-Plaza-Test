from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Ingredient(models.Model):
    text = models.CharField(max_length=150, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default = '0', related_name='ingredients')


class Step(models.Model):
    step_text = models.CharField(max_length=150, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default = '0', related_name='steps')


