from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    ordering = ['-posted_date']

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class AddRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_message = 'Your thing has been done successfully'
    
class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    fields = ['title', 'description']

class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('recipe_view')
    
