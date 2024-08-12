from django import forms
from django.core.exceptions import ValidationError
from .models import Recipe

CHART_CHOICES = (
    ('bar', 'Bar chart'),
    ('pie', 'Pie chart'),
    ('line', 'Line chart')
)

class RecipeSearchForm(forms.Form):
    recipe_title = forms.CharField(max_length=120, required=False, label="Recipe Name")
    description = forms.CharField(max_length=300, required=False, label="Description")
    ingredients = forms.CharField(max_length=300, required=False, label="Ingredients")
    preparation = forms.CharField(max_length=300, required=False, label="Preparation")
    min_cooking_time = forms.IntegerField(required=False, label="Min Cooking Time")
    max_cooking_time = forms.IntegerField(required=False, label="Max Cooking Time")
    category = forms.ChoiceField(
    choices=Recipe.CATEGORY_CHOICES,
    required=False,
    label="Category"
)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False, label="Chart Type")
    created_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Date Created")

    def clean(self):
        cleaned_data = super().clean()
        min_cooking_time = cleaned_data.get("min_cooking_time")
        max_cooking_time = cleaned_data.get("max_cooking_time")
        created_date = cleaned_data.get("created_date")
        
        if min_cooking_time is not None and max_cooking_time is not None and min_cooking_time > max_cooking_time:
            raise ValidationError("Min Cooking Time cannot be greater than Max Cooking Time")

        return cleaned_data
