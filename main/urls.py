""" main/urls.py """
from django.urls import path
from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film,\
                    nowy_review, wszystkie_reviews,search_filmy, film_detail,  new_actor,lista_aktorow, usun_aktora,\
                    actor_detail, actor_edit, new_actor_in_movie, new_actor_in_movie_dt,\
                    adding_actor_from_new_actor_in_movie_dt
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, MovieViewSet, ActorViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('filmy/', wszystkie_filmy, name = 'wszystkie_filmy'),
    path('search/', search_filmy, name = 'search_filmy'),
    path('nowy_film/', nowy_film, name = 'nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name = 'edytuj_film'),
    path('film_detail/<int:id>/', film_detail, name = 'film_detail'),
    path('new_actor_in_film/<int:id>/', new_actor_in_movie, name = 'new_actor_in_movie'),
    path('new_actor_in_movie_dt/<int:id>/', new_actor_in_movie_dt, name = 'new_actor_in_movie_dt'),
    path('adding_actor_from_new_actor_in_movie_dt/<int:id>/', adding_actor_from_new_actor_in_movie_dt, name = 'adding_actor_from_new_actor_in_movie_dt'),
    path('actor_detail/<int:id>/', actor_detail, name = 'actor_detail'),
    path('usun/<int:id>/', usun_film, name = 'usun_film'),
    path('usun_aktora/<int:id>/', usun_aktora, name = 'usun_aktora'),
    path('edytuj_actor/<int:id>/', actor_edit, name = 'actor_edit'),
    path('filmy/<int:id>/new_review', nowy_review, name = 'nowy_review'),
    path('filmy/<int:id>/reviews', wszystkie_reviews, name = 'wszystkie_reviews'),
    path('nowy_aktor/', new_actor, name = 'new_actor'),
    path('aktorzy/', lista_aktorow, name = 'lista_aktorow'),

    url(r'^', include(router.urls))
]
