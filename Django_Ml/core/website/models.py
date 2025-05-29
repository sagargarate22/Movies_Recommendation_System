from django.db import models
from django.db import models

class Movies(models.Model):
    movie_name = models.TextField(max_length=100)

    def __str__(self):
        return self.movie_name