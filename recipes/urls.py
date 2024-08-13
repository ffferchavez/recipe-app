# recipes/urls.py
from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeDeleteView, home, search

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('recipes/', RecipeListView.as_view(), name='list'),  # List view for recipes
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='detail'),  # Detail view for a single recipe
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='delete'),  # New: Delete view for a single recipe (Admin only)
    path('search/', search, name='search'),  # Search functionality
]
