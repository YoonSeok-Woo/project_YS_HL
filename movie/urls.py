from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/rating/',views.rating,name='rating'),
    path('recommendtation/',views.recommend,name='recommend'),
]
