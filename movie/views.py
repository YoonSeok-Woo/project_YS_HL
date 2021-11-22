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
    return render(request, 'movies/home.html', context)