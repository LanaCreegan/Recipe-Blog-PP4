from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def LikeRecipe(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_like_id'))
    liked = False
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
    else:
        recipe.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('recipe_detail', args=[str(pk)]))


class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    ordering = ['-posted_date']
    paginate_by = 4

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(*args, **kwargs)
        recipe_likes = get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_likes = recipe_likes.total_likes()

        liked = False
        if recipe_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddRecipeView(SuccessMessageMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_message = 'The recipe was successfully added'

    
class UpdateRecipeView(SuccessMessageMixin, UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    fields = ['title', 'description']
    success_message = 'The post was successfully updated'


def delete_recipe(request, recipe_id):
    """
    Delete Book
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    messages.success(request, 'The post was deleted successfully')
    return redirect('recipe_view')
    
    
    
