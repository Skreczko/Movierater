
""" main/ forms.py """
from django.forms import ModelForm
from django import forms
from .models import Movie, ExtraInfo, Review, Actor

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['info']

class MovieInfoForm(ModelForm):
    class Meta:
        model = Movie
        exclude = []


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = []

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'text']

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        exclude = ["movie"]

class Actor_MovieForm(ModelForm):
    class Meta:
        model = Actor
        exclude = []
