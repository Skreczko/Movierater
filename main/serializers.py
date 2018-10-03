"""  movierater/main/serializers.py"""
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo, Actor, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'url', 'username', 'email')

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields  = ('czas_trwania', 'rodzaj')

class MovieForActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year')

class MovieSerializer(serializers.ModelSerializer):
    info = InfoSerializer(many=False)
    class Meta:
        model = Movie
        fields = ('id','info', 'name', 'year', 'description',  'released', 'imdb_rating')

class ActorSerializer(serializers.ModelSerializer):
    movie = MovieForActorsSerializer(many=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'last_name', 'biography', 'movie')


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieForActorsSerializer(many=False)
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'published_date', 'movie')






