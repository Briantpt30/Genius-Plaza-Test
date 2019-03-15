from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    text = models.CharField(max_length=150, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default = '0', related_name='ingredients')
    def __str__(self):
        return self.text


class Step(models.Model):
    step_text = models.CharField(max_length=150, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default = '0', related_name='steps')
    def __str__(self):
        return self.step_text