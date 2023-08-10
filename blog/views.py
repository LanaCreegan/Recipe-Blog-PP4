from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class AddRecipeView(CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    fields = '__all__'