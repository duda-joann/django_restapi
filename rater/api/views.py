from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
from django.http.response import HttpResponseBadRequest
from .serializers import (
                        UserSerializer,
                        MovieSerializer,
                        DirectorSerializer,
                        ActorSerializer,
                        ReviewSerializer,
                          )
from .models import *
from django.db.models.query import QuerySet
from django.http import HttpRequest


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class MovieViewSet(viewsets.ModelViewSet):
    """ Api endpoint that allows to view and edit movies"""
    serializer_class = MovieSerializer
    ordering = ('the_premier',)
    pagination_class = MovieSetPagination
    filter_fields = ['id', 'year', 'title']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissions, )

    def get_queryset(self) -> QuerySet[Movie]:
        movies = Movie.objects.all()
        return movies

    def retrieve(self, request: HttpRequest, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)

    def create(self, request: HttpRequest, *args, **kwargs) -> Response:
        if request.user.is_staff:
            movie = Movie.objects.create(
                title = request.data['title'],
                description = request.data['description'],
                year = request.data['year'],
                last = request.data['last'],
                the_premiere = request.data['the_premiere'],

            )
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        return HttpResponseBadRequest()

    def update(self, request: HttpRequest, *args, **kwargs) -> Response:
        movie = self.get_object()
        movie.title = request.data['title']
        movie.description = request.data['description']
        movie.the_premiere = request.data['the_premiere']
        movie.save()

        serializer = MovieSerializer(movie, many=False)

        return Response(serializer.data)

    def delete(self, request: HttpRequest, *args, **kwargs) -> Response:
        movie = self.get_object()
        movie.delete()
        return Response('Record has been removed')

    @action(detail=False, methods=['post'])
    def is_premiere(self, request: HttpRequest, *args, **kwargs) -> Response:
        movies = Movie.objects.all()
        movies.after_the_premiere = True
        movies.save()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)


class ActorViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows view or edit actors
    """
    serializer_class = ActorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self) -> QuerySet[Actor]:
        queryset = Actor.objects.all()
        return queryset

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = ActorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = ActorSerializer(instance)
        return Response(serializer.data)

    def delete(self, request) -> Response:
        actor = self.get_object()
        actor.delete()
        return Response('Record has been removed')

    @action(detail=True, methods=['post'])
    def join(self, request, **kwargs) -> Response:
        actor = self.get_object()
        movie = Movie.objects.get(id=request.data['movies'])
        actor.movies.add(movie)
        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows  reviews to be viewed or edited.
        """
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self) -> QuerySet[Review]:
        queryset = Review.objects.all()
        return queryset

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = ReviewSerializer(instance)
        return Response(serializer.data)

    def delete(self, request) -> Response:
        review = self.get_object()
        review.delete()
        return Response('Record has been removed')


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    authentication_classes = (TokenAuthentication,)
    depth = 2

    def get_queryset(self)-> QuerySet[Director]:
        directors = Director.objects.all()
        return directors

    def list(self, request: HttpRequest, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: HttpRequest, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = DirectorSerializer(instance)
        return Response(serializer.data)

    def delete(self, request: HttpRequest, *args, **kwargs) -> Response:
        director = self.get_object()
        director.delete()
        return Response('Record has been removed')

    @action(detail=True, methods=['post'])
    def join(self, request, **kwargs) -> Response:
        director = self.get_object()
        movie = Movie.objects.get(id=request.data['movies'])
        director.movies.add(movie)
        serializer = DirectorSerializer(director, many=False)
        return Response(serializer.data)