from rest_framework import serializers
from api.models import Movie


class MovieSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'after_the_premiere',  'the_premiere', 'year', 'last', 'imdb']