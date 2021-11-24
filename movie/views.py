from typing import Reversible
from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods,require_GET
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Movie, Genre, Rates
from django.db.models import Avg, Q
from django.http.response import JsonResponse, HttpResponse
from .serializer import MoiveSerializer
from django.core import serializers
import json
@require_GET
def home(request):
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies':movies
    }
    return render(request, 'movie/home.html', context)
def random(request):
    movies = Movie.objects.order_by('?')[:10]
    data = []
    for movie in movies:
        data.append({
            'posterpath':movie.poster_path,
        })
    return JsonResponse({'data':data}, json_dumps_params={'ensure_ascii':False},status=200)
@require_http_methods(['GET','POST'])
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie
    }
    return render(request, 'movie/detail.html',context)

def rating(request, pk):
    user = request.user
    print(user)

    score = json.loads(request.body).get('rates')
    print(score)
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
        rated_status = {
            'score': score,
            'average_rate': movie.average_rate
        }
        return JsonResponse(rated_status)
    
    return HttpResponse(status=401)

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
@require_GET
def genre_list(request):
    genres = Genre.objects.all()
    data = []
    for genre in genres:
        data.append({
            'pk':genre.pk,
            'genre_name':genre.name,
        })
    return JsonResponse({'data':data}, json_dumps_params={'ensure_ascii':False},status=200)

@require_GET
def genre_movies(request,pk):
    genre = get_object_or_404(Genre,pk=pk)
    movies = Movie.objects.filter(genres=genre)
    paginator = Paginator(movies, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        "movies" : movies,
        "posts" : posts,
    }
    return render(request, 'movie/genre_list.html', context)

@require_http_methods(['GET','POST'])
def search(request):
    #searchword = json.loads(request.body).get('search')
    
    return render(request, 'movie/searchbar.html')
        
def searchword(request,searchword):
    
    movies = Movie.objects.filter(Q(title__icontains=searchword)|Q(overview__icontains=searchword))
    paginator = Paginator(movies,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    data = []
    for movie in posts:
        data.append({
            'pk':movie.pk,
            'title':movie.title,
            'overview':movie.overview,
            'posterpath':movie.poster_path,
            'average_rate':movie.average_rate,
        })
    post_data = {
        'has_next':posts.has_next(),
        'has_previous':posts.has_previous(),
        'num_pages':posts.paginator.num_pages
    }
    return JsonResponse({'data':data,'posts':post_data}, json_dumps_params={'ensure_ascii':False},status=200)
