from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/movies', views.MovieViewSet, basename="Movie")
router.register(r'api/actors', views.ActorViewSet, basename="Actors")
router.register(r'api/directors', views.DirectorViewSet, basename="Director")
router.register(r'api/reviews', views.ReviewViewSet, basename='Review')


urlpatterns = [
    url(r'^', include(router.urls))
]