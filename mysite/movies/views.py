from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActionMovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(genre='Action')
    serializer_class = MovieSerializer