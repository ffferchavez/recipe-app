# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RecipeSearchForm
from ingredients.models import Ingredient
from django.db.models import Q, Count
from .utils import generate_chart
import pandas as pd

# List view for displaying all recipes
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'
    context_object_name = 'recipes'

# Detail view for a specific recipe
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe'

# New: Delete view for a specific recipe (Admin only)
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes:list')

    def test_func(self):
        # Only allow admin users to delete recipes
        return self.request.user.is_superuser

# Home view
def home(request):
    return render(request, 'recipes/recipes_home.html')

# Search view to handle recipe search form submission
def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipes = Recipe.objects.all()
    chart = None

    if form.is_valid():
        search_title = form.cleaned_data.get('recipe_title')
        search_description = form.cleaned_data.get('description')
        search_ingredients = form.cleaned_data.get('ingredients')
        search_preparation = form.cleaned_data.get('preparation')
        min_cooking_time = form.cleaned_data.get('min_cooking_time')
        max_cooking_time = form.cleaned_data.get('max_cooking_time')
        created_date = form.cleaned_data.get('created_date')
        category = form.cleaned_data.get('category')
        chart_type = form.cleaned_data.get('chart_type')

        if search_title:
            recipes = recipes.filter(title__icontains=search_title)
        if search_description:
            recipes = recipes.filter(description__icontains=search_description)
        if search_ingredients:
            ingredient_ids = Ingredient.objects.filter(name__icontains=search_ingredients).values_list('id', flat=True)
            recipes = recipes.filter(ingredients__in=ingredient_ids).distinct()
        if search_preparation:
            recipes = recipes.filter(preparation__icontains=search_preparation)
        if min_cooking_time is not None:
            recipes = recipes.filter(cooking_time__gte=min_cooking_time)
        if max_cooking_time is not None:
            recipes = recipes.filter(cooking_time__lte=max_cooking_time)  # <-- Fixed missing closing parenthesis here
        if created_date:
            recipes = recipes.filter(created_at__date=created_date)
        if category:
            recipes = recipes.filter(category=category)

        # Prepare data for charting
        if recipes:
            if chart_type == 'bar':
                data = recipes.values('cooking_time').annotate(count=Count('id'))
                chart = generate_chart('bar', data)
            elif chart_type == 'pie':
                data = recipes.values('preparation').annotate(count=Count('id'))
                chart = generate_chart('pie', data)
            elif chart_type == 'line':
                data = recipes.values('created_at').annotate(count=Count('id')).order_by('created_at')
                chart = generate_chart('line', data)

    context = {
        'form': form,
        'recipes': recipes,
        'chart': chart
    }

    return render(request, 'recipes/search_results.html', context)
