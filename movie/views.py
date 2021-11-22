from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods,require_GET
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Rates

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
def rating(request,pk,score):
    user = request.user
    if user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if user in movie.rates
    return redirect('user:login')

@require_GET
def recommend(request):
    user = request.user
    if user.is_authenticated:
        movies = user.movies.all()
        if len(movies)>=10:
            genres_count = dict()
            for movie in movies:
                movie_genres = movie.genres
                for genre in movie_genres:
                    if genres_count[genre]:
                        genres_count[genre]+=1
                    else:
                        genres_count[genre]=1
            favorite = max(genres_count)
            output = Movie.objects.filter(genres=favorite).order_by('?')[:10]
            context = {
                'movie': output
            }
            return render(request,'movie/recommend.html')
    
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movie':movies
    }
    return render(request, 'movie/recommend.html', context)
    