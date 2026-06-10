from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User


class Actor(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=(('male', 'male'), ('female', 'female')))
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name



class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment








