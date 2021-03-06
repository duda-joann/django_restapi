from rest_framework import serializers
from api.models import Movie

class MovieMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year']