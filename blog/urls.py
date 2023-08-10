from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeView.as_view(), name='recipe_view'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
]