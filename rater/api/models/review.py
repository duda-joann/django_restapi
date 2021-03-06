from django.db import models
from .movie import Movie

# Create your models here.


class Review(models.Model):
    description = models.TextField(default = "Your review")
    stars = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name= "Review" )