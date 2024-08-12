from django.db import models
from ingredients.models import Ingredient
from django.shortcuts import reverse
from django.utils import timezone

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='breakfast')
    ingredients = models.ManyToManyField(Ingredient)
    preparation = models.TextField(blank=True, null=True)
    cooking_time = models.IntegerField(help_text="in minutes")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    created_at = models.DateTimeField(default=timezone.now)

    def calculate_difficulty(self):
        ingredient_count = self.ingredients.count()
        if self.cooking_time < 10 and ingredient_count < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            return "Intermediate"
        else:
            return "Hard"

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
