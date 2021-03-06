from rest_framework import serializers
from .movieminiserializer import MovieMiniSerializer
from  api.models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    movies = MovieMiniSerializer(source="review", many=True)

    class Meta:
        model = Review
        fields = ['id', 'description', 'stars', 'movies']

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.save()

        return instance
