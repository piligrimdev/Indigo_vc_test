from django.db import models


class User(models.Model):
    name = models.CharField()
    birthday = models.DateField()

class Movie(models.Model):
    name