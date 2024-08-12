from django.test import TestCase
from .models import Ingredient

class IngredientTestCase(TestCase):
    def setUp(self):
        Ingredient.objects.create(name="Salt")

    def test_ingredient_creation(self):
        ingredient = Ingredient.objects.get(name="Salt")
        self.assertEqual(ingredient.name, "Salt")
