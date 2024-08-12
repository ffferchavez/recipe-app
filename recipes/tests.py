from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Recipe
from .forms import RecipeSearchForm
from ingredients.models import Ingredient

class RecipeTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Sugar")
        self.recipe = Recipe.objects.create(title="Cake", description="Delicious cake", cooking_time=30)
        self.recipe.ingredients.add(self.ingredient)

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
        self.assertEqual(recipe.get_absolute_url(), f'/recipes/{recipe.id}/')  # Adjusted expected URL

class RecipeSearchFormTestCase(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'recipe_title': 'Cake',
            'description': 'Delicious cake',
            'ingredients': 'Sugar',
            'preparation': 'Mix and bake',
            'min_cooking_time': 20,
            'max_cooking_time': 40,
            'category': 'dessert',  # Ensure this is a valid category
            'chart_type': 'bar',
            'created_date': '2024-08-12'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'min_cooking_time': 50,
            'max_cooking_time': 40  # Invalid, min > max
        }
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'], ["Min Cooking Time cannot be greater than Max Cooking Time"])

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Cake",
            description="Delicious cake",
            cooking_time=30,
            category="dessert"
        )
        self.recipe.ingredients.add(Ingredient.objects.create(name="Sugar"))
        self.url = reverse('search')  # Replace with your actual URL name

    def test_search_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/search_results.html')  # Adjusted to check the correct template name

    def test_search_view_post_valid(self):
        form_data = {
            'recipe_title': 'Cake',
            'category': 'dessert',
            'chart_type': 'bar'
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cake')
        self.assertContains(response, 'Chart')

    def test_search_view_post_invalid(self):
        form_data = {
            'min_cooking_time': 50,
            'max_cooking_time': 40  # Invalid, min > max
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Min Cooking Time cannot be greater than Max Cooking Time")
