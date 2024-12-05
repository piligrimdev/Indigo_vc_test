from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя пользователя', max_length=40)
    second_name = models.CharField(verbose_name='Фамилия пользователя', max_length=40)
    birthday = models.DateField(verbose_name='Дата рождения')


class Movie(models.Model):
    name = models.CharField(verbose_name='Название фильма', max_length=250, blank=False, null=False)
    rating = models.SmallIntegerField(verbose_name='Рейтинг', default=5,
                                      validators=[
                                          MaxValueValidator(10),
                                          MinValueValidator(0)
                                      ])
    release_date = models.DateField(verbose_name='Дата выхода', null=False, blank=False)
    age_restriction = models.BooleanField(verbose_name='Наличие возрастного ограничения', default=False)
