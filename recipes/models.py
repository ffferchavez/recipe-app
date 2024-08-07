from django.db import models
from ingredients.models import Ingredient

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title
