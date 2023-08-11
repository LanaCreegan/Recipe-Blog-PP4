from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form for Recipe"""

    class Meta:
        model = Recipe
        fields = ('title', 'author', 'description', 'overview')