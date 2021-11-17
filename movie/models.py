from django.db import models
from django.db.models.fields import related
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    average_rank = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
    rate = models.ManyToManyField(settings.AUTH_USER_MODEL,through='Rates',related_name='movies',)
    
class Rates(models.Model):
    RATES = (
        (1,'★☆☆☆☆'),
        (2,'★★☆☆☆'),
        (3,'★★★☆☆'),
        (4,'★★★★☆'),
        (5,'★★★★★'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='rates',on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='rates',on_delete=models.CASCADE)
    rates = models.IntegerField(choices = RATES, default = 5)
class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name = 'movies')
