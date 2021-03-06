from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length = 400)
    after_the_premiere = models.BooleanField(default=False)
    the_premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    last = models.IntegerField()
    imdb = models.DecimalField(default=0, max_digits=4, decimal_places=3,  null=True, blank=True)

    def render_name(self):
        return f'{self.title} + " " + {str(self.year)}'

    def __str__(self):
        return self.render_name()