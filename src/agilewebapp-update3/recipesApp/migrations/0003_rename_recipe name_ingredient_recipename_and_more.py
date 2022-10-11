# Generated by Django 4.0.2 on 2022-03-01 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesApp', '0002_rename_recipename_ingredient_recipe name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe name',
            new_name='recipeName',
        ),
        migrations.RenameField(
            model_name='nutrient',
            old_name='recipe name',
            new_name='recipeName',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cooking time',
            new_name='cookingTime',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='date added',
            new_name='dateAdded',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe category',
            new_name='recipeCategory',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='skills level',
            new_name='skillsLevel',
        ),
    ]