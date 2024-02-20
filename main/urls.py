"""
URL configuration for main app.
"""
from django.urls import path

from .views import MoviesListView, MovieDetailsView, NewReviewView


app_name = 'main'
urlpatterns = [
    path('', MoviesListView.as_view(), name='movies-list'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
    path('movie/<int:movie_pk>/review/', NewReviewView.as_view(), name='new-review'),
]