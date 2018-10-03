
import calendar
from django.db import models


# Create your models here.
class ExtraInfo(models.Model):
    RODZAJE = (
        (0, 'nieznany'),
        (1, 'komedia'),
        (2, 'dramat'),
        (3, 'sci-fi'),
        (4, 'kryminal')
    )

    czas_trwania = models.IntegerField(default=0)
    rodzaj = models.IntegerField(default=0 , choices=RODZAJE)

    def __str__(self):
        return str(self.RODZAJE[self.rodzaj][1]) + ":  " + str(self.czas_trwania)+"min"

class Movie(models.Model):
    name = models.CharField(max_length=128)  # charfield - string
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo = models.ImageField(null=True, blank=True, upload_to='filmy')
    info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name_with_year()
    def name_with_year(self):
        return str(self.name) + " ({})".format(str(self.year))


class Review(models.Model):
    RODZAJE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    text = models.CharField(default="", max_length=500, blank=True, verbose_name='Komentarz')
    stars = models.IntegerField(default=5, verbose_name='Ocena', choices=RODZAJE)
    published_date = models.DateTimeField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie) + " stars: " + str(self.stars) + " " + str(self.text[:5]) + "..."


class Actor(models.Model):
    name = models.CharField(max_length=128,verbose_name='Imię', default="")
    last_name = models.CharField(max_length=128, verbose_name='Nazwisko', default="")
    photo = models.ImageField(null=True, blank=True, upload_to='actors')
    biography = models.CharField(default="", max_length=500, blank=True, verbose_name='Biografia')
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return str(self.name) + " " + str(self.last_name)