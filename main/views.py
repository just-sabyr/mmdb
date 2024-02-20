from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView

from main.models import MovieDetails, MovieReview

from django.utils.translation import get_language, activate
from django.conf import settings

class MoviesListView(ListView):
    model = MovieDetails
    template_name = 'movies_list.html'

    def render_to_response(self, context, **response_kwargs):

        user_language = get_language() # get the current language set by the user
        activate(user_language)        # activate the language

        response = super(MoviesListView, self).render_to_response(context, **response_kwargs)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        return response

    

class MovieDetailsView(DetailView):
    model = MovieDetails
    template_name = 'movie_details.html'


class NewReviewView(CreateView):
    model = MovieReview
    fields = ['user_name', 'review']

    template_name = 'new_movie_review.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewReviewView, self).get_context_data(**kwargs)

        movie_pk = self.kwargs['movie_pk']
        movie = MovieDetails.objects.get(pk=movie_pk)
        ctx['movie'] = movie

        return ctx

    def form_valid(self, form):
        movie_pk = self.kwargs['movie_pk']
        movie = MovieDetails.objects.get(pk=movie_pk)

        review = form.save(commit=False)
        review.movie = movie
        review.save()

        return HttpResponseRedirect(reverse('main:movie-details', kwargs={'pk': movie_pk}))
