from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CATEGORY_CHOICES = [
    ('appetizer', 'Appetizer'),
    ('main_course', 'Main Course'),
    ('dessert', 'Dessert'),
    ('salad', 'Salad'),
    ('soup', 'Soup'),
    ('side_dish', 'Side Dish'),
    ('beverage', 'Beverage'),
    ('snack', 'Snack'),
    ('breakfast', 'Breakfast'),
    ('bread', 'Bread'),
    ('pasta', 'Pasta'),
    ('seafood', 'Seafood'),
    ('grill', 'Grill'),
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
]

class Recipe(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.JSONField()
    instructions = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    preparation_time = models.IntegerField(help_text='Time in minutes', validators=[MinValueValidator(0)])
    cooking_time = models.IntegerField(help_text='Time in minutes', validators=[MinValueValidator(0)], blank=True, null=True)
    servings = models.IntegerField(validators=[MinValueValidator(1)], help_text='Number of servings')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title

class RateAndReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    review = models.TextField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user} reviewed {self.recipe.title} - Rating: {self.rating}"
