from django.test import TestCase
from .models import Recipe
from ingredients.models import Ingredient

class RecipeTestCase(TestCase):
    def setUp(self):
        ingredient = Ingredient.objects.create(name="Sugar")
        recipe = Recipe.objects.create(title="Cake", description="Delicious cake", cooking_time=30)
        recipe.ingredients.add(ingredient)

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(title="Cake")
        self.assertEqual(recipe.title, "Cake")
        self.assertEqual(recipe.description, "Delicious cake")
        self.assertEqual(recipe.cooking_time, 30)

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(title="Cake")
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 1)
        self.assertEqual(ingredients.first().name, "Sugar")

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(title="Cake")
        self.assertEqual(recipe.get_absolute_url(), f'/list/{recipe.id}/')
