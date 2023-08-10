from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeView.as_view(), name='recipe_view'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/edit/<int:pk>', views.UpdateRecipeView.as_view(), name='update_recipe'),
    path('recipe/<int:pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]