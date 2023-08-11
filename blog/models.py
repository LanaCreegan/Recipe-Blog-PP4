from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import datetime, date


class Recipe(models.Model):
    """Model for Recipe"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField(blank=True)
    description = models.TextField(max_length=5000, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    posted_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='recipe_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('recipe_view')


