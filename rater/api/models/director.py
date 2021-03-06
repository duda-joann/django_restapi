from django.db import models
from .movie import Movie

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField(max_length = 500)
    movies = models.ManyToManyField(Movie)