from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User


# Here are models like Recipe mapped to the database
class Recipe(models.Model):
    skillsChoice = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Difficult', 'Difficult')
    )
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Anonymous')
    recipeName = models.CharField(max_length=120, primary_key=True)
    cost = models.DecimalField(max_digits=5, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.01'), message='The cost may not be less than 0.01 £')])
    portion = models.PositiveSmallIntegerField(default=1,
                                               validators=[MaxValueValidator(20, message='To many portions')])
    description = models.TextField(
        validators=[MinLengthValidator(5, message='Please provide longer description')])
    guide = models.TextField(default='Step 1: ',
                             validators=[MinLengthValidator(10, message='Please provide longer guide')])
    cookingTime = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120, message='The cooking time is too long')])
    skillsLevel = models.CharField(max_length=30, choices=skillsChoice)
    dateAdded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.recipeName


class Ingredient(models.Model):
    recipeName = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=120)

    def __str__(self):
        return 'Author: %s, Recipe: %s - %s' % (self.recipeName.author, self.recipeName, self.ingredient)


class Nutrient(models.Model):
    recipeName = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    calories = models.PositiveSmallIntegerField(default=0,
                                                validators=[MaxValueValidator(3000, message='To many calories')])
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=None,
                              validators=[MinValueValidator(Decimal('-0.01'), message='Fat must not be less than 0'),
                                          MaxValueValidator(500, message='Too much fat')])
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=None,
                                       validators=[
                                           MinValueValidator(Decimal('-0.01'),
                                                             message='Carbohydrate must not be less than 0'),
                                           MaxValueValidator(500, message='Too much carbohydrate')])
    fibre = models.DecimalField(max_digits=5, decimal_places=2, default=None,
                                validators=[
                                    MinValueValidator(Decimal('-0.01'), message='Fibre must not be less than 0'),
                                    MaxValueValidator(500, message='Too much fibre')])
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=None,
                                  validators=[
                                      MinValueValidator(Decimal('-0.01'), message='Protein must not be less than 0'),
                                      MaxValueValidator(500, message='Too much protein')]
                                  )
    salt = models.DecimalField(max_digits=5, decimal_places=2, default=None,
                               validators=[MinValueValidator(Decimal('-0.01'), message='Salt must not be less than 0'),
                                           MaxValueValidator(500, message='Too much salt')])

    def __str__(self):
        return 'Author: %s, Recipe: %s' % (self.recipeName.author, self.recipeName)
