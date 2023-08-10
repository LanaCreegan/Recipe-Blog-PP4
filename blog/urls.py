from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeView.as_view(), name='recipe_view')
]