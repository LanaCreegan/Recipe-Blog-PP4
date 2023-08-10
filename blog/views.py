from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class AddRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'

class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    fields = ['title', 'description']

class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    
