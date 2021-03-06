from django.db import models
from .movie import Movie

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField(max_length = 500)
    birth = models.DateField(null=True, blank=True)
    movies = models.ManyToManyField(Movie)