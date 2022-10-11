# Generated by Django 4.0.2 on 2022-03-01 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipeName',
            new_name='recipe name',
        ),
        migrations.RenameField(
            model_name='nutrient',
            old_name='recipeName',
            new_name='recipe name',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cookingTime',
            new_name='cooking time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='dateAdded',
            new_name='date added',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeCategory',
            new_name='recipe category',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeName',
            new_name='recipe name',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='skillsLevel',
            new_name='skills level',
        ),
    ]