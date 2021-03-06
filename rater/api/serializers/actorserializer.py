from rest_framework import serializers
from api.models import Actor
from api.models import Movie
from .movieminiserializer import MovieMiniSerializer


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Actor
        fields = ['name', 'surname', 'bio', 'birth', 'movies']

    def create(self, validated_data):
        movies = validated_data['movies']
        del validated_data['movies']

        actor = Actor.objects.create(**validated_data)

        for movie in movies:
            m = Movie.objects.create(**movie)
            actor.movies.add(m)

        actor.save()

        return actor