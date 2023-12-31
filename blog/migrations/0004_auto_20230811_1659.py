# Generated by Django 3.2.20 on 2023-08-11 16:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_recipe_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
