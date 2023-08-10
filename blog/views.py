from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeView(ListView):
    model = Recipe
    template_name = 'base.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'