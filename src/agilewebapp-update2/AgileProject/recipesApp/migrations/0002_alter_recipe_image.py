# Generated by Django 4.0.2 on 2022-02-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.URLField(max_length=2083),
        ),
    ]