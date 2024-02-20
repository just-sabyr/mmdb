from django.db import models


class MovieDetails(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    movie = models.ForeignKey(MovieDetails, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    review = models.TextField()
