# Generated by Django 3.2.20 on 2023-08-11 08:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_recipe_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='recipe_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
