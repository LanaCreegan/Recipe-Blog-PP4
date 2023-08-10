from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeView(ListView):
    model = Recipe
    template_name = 'base.html'
