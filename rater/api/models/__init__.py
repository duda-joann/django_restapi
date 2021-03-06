from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .movie import Movie
from .actor import Actor
from .review import Review
from .director import Director


@receiver(post_save, sender=User)
def token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)