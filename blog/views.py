from django.shortcuts import render
from django.views.generic import ListView, DetailView

class RecipeView(ListView):
    model = Recipe
    template_name = 'base.html'
