from django.db import models

from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    intro = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    image = models.ImageField(upload_to='images/', default='image/default.jpg')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('recipe-detail', args=[str(self.id)])

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        ordering = ['name',]


    def __str__(self):
        return self.name