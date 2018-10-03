#views.py
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Actor
from .forms import MovieForm, ExtraInfoForm, MovieInfoForm, ReviewForm, ActorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer, ActorSerializer, ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



def wszystkie_filmy(request):
    filmy = Movie.objects.all()
    actor = Actor.objects.all()
    return render(request, 'lista_filmow.html',
                  { 'filmy': filmy, 'actor': actor } )




def search_filmy(request):
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('q', None)
        filmy = Movie.objects.filter(name = search_query)
        if search_query == "" :
            return redirect(wszystkie_filmy)
        return render(request, 'lista_filmow.html', {'filmy': filmy})

@login_required
def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html',
                  {'form': form})


@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Movie, pk = id)            #primary key
    form = MovieInfoForm(request.POST or None, request.FILES or None,
                     instance=film)
    info = ExtraInfoForm(request.POST or None, instance=film.info)
    if form.is_valid():
        form.save()
        info.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html',
                  {'form': form, 'info': info})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Movie, pk=id)  # primary key
    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html',
                  {'film': film})

@login_required
def nowy_review(request, id):
    film = get_object_or_404(Movie, pk=id)
    review = ReviewForm(request.POST)
    if review.is_valid():
        post = review.save(commit=False)
        post.movie = film
        post.published_date = timezone.now()
        post.save()
        return redirect(wszystkie_reviews, film.id)
    return render(request, 'review_form.html', {'review':review})

def wszystkie_reviews(request, id):
    film = get_object_or_404(Movie, pk=id)
    review = Review.objects.filter(movie=film).order_by('-published_date')
    return render(request, 'lista_review.html',
                  {'review': review, 'film': film})


@login_required
def new_actor(request):
    actor = ActorForm(request.POST or None, request.FILES or None)
    if actor.is_valid():
        actor.save()
        return redirect(lista_aktorow)
    return render(request, 'review_form.html', {'review':actor})

def lista_aktorow(request):
    form = Actor.objects.all().order_by('last_name')
    return render(request, 'lista_aktorow.html',
                  { 'form': form } )

def actor_detail(request, id):
    actor = get_object_or_404(Actor, pk=id)
    return render(request, 'actor_detail.html',
                  {'actor': actor})

def actor_edit(request, id):
    actor = get_object_or_404(Actor, pk=id)
    form = ActorForm(request.POST or None, request.FILES or None, instance=actor)
    if form.is_valid():
        form.save()
        return redirect(lista_aktorow)
    return render(request, 'review_form.html',
                  {'review': form})

def usun_aktora(request, id):
    actor = get_object_or_404(Actor, pk=id)  # primary key
    if request.method == 'POST':
        actor.delete()
        return redirect(lista_aktorow)

    return render(request, 'potwierdz_actor.html',
                  {'actor': actor})


def new_actor_in_movie(request, id):
    film = get_object_or_404(Movie, pk=id)
    actor = ActorForm(request.POST or None, request.FILES or None)
    if actor.is_valid():
        post = actor.save()
        post.movie.add(film)
        post.save()
        return redirect(film_detail, film.id)

    return render(request, 'review_form.html', {'review': actor})

def new_actor_in_movie_dt(request, id):
    form = Actor.objects.all().order_by('last_name')
    film = get_object_or_404(Movie, pk=id)
    def newwww():
        post = form.save()
        post.movie.add(film)
        post.save()
    return render(request, 'aktor_form_db.html',
                  {'form': form , 'film': film})

def adding_actor_from_new_actor_in_movie_dt(request, id_film, id_actor):
    actor = get_object_or_404(Movie, pk=id_actor)
    film = get_object_or_404(Movie, id=id_film)
    actor.movie.add(film)
    if actor.is_valid():
        post = actor.save()
        post.movie.add(film)
        post.save()
        return redirect(film_detail, film.id)


    return render(None, 'aktor_form_db.html',
                  {'form': film , 'film': film})




def film_detail(request, id):
    film = get_object_or_404(Movie, pk = id)
    return render(request, 'film_detail.html',
                  { 'film': film} )