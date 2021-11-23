from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/rating/',views.rating,name='rating'),
    path('recommend/',views.recommend,name='recommend'),
    path('genre_list/',views.genre_list,name='genre_list'),
    path('genre/<int:pk>/',views.genre_movies,name='genre_movies'),
    path('search/', views.search, name= 'search'),
]
