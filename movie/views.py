from typing import Reversible
from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods,require_GET
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Rates
from django.db.models import Avg
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

@require_GET
def home(request):
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies':movies
    }
    return render(request, 'movie/home.html', context)

@require_http_methods(['GET','POST'])
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie
    }
    return render(request, 'movie/detail.html',context)

@require_POST
def rating(request,pk):
    user = request.user
    score = request.POST.get('rates')
    
    if user.is_authenticated:
        movie = get_object_or_404(Movie,pk=pk)
        if movie.rate.filter(pk=user.pk).exists():
            t_rates = Rates.objects.get(user_id=user,movie_id=movie)
            t_rates.rates=score
            t_rates.save()
        else:
            
            new_rates=Rates()
            new_rates.user=user
            new_rates.rates=score
            new_rates.movie=movie
            new_rates.save()
        movie.average_rate=Rates.objects.filter(movie_id=movie).aggregate(Avg('rates'))['rates__avg']
        movie.save()
        return redirect('movie:detail',pk)
    
    return redirect('user:login')

@require_GET
def recommend(request):
    user = request.user
    if user.is_authenticated:
        movies = user.movies.all()
        if len(movies)>=10:
            genres_count = dict()
            for movie in movies:
                movie_genres = movie.genres.all()
                for genre in movie_genres:
                    if genre.name in genres_count:
                        genres_count[genre.name]+=1
                    else:
                        genres_count[genre.name]=1
            favorite = max(genres_count)
            t_genres = Genre.objects.get(name=favorite)
            output = Movie.objects.filter(genres=t_genres).order_by('?')[:10]
            context = {
                'movies': output
            }
            return render(request,'movie/recommend.html', context)
    
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies':movies
    }
    return render(request, 'movie/recommend.html', context)

def genre_list(request):
    genres = Genre.objects.all()
    data = []
    for genre in genres:
        data.append({
            'pk':genre.pk,
            'genre_name':genre.name,
        })
    return JsonResponse({'data':data}, json_dumps_params={'ensure_ascii':False},status=200)


