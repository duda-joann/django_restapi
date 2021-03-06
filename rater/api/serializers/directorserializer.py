from rest_framework import serializers
from .movieminiserializer import MovieMiniSerializer
from api.models import Director


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'surname', 'bio', 'movies']