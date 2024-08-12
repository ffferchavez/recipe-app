# recipes/urls.py
from django.urls import path
from . import views

app_name = 'recipes'  # Namespace for URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='list'),
    path('list/<pk>/', views.RecipeDetailView.as_view(), name='detail'),
]
