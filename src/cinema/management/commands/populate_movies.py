"""
Заполняет таблицу с фильмами
"""

from django.core.management import BaseCommand
from django.db import transaction

from cinema.models import Movie

import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Creating movies")

            movie1, flag = Movie.objects.get_or_create(
                name="Very epic movie", rating=4, release_date=datetime.date(year=1984, month=5, day=4)
            )

            movie2, flag = Movie.objects.get_or_create(
                name="Very epic movie 2:electric boogaloo", rating=2, release_date=datetime.date(year=1984, month=12, day=21)
            )

            movie3, flag = Movie.objects.get_or_create(
                name="Disney Fantasy", rating=10, release_date=datetime.date(year=1940, month=11, day=13)
            )

            movie4, flag = Movie.objects.get_or_create(
                name="Scarface", rating=10, release_date=datetime.date(year=1983, month=12, day=9),
                age_restriction=True
            )

            self.stdout.write(self.style.SUCCESS("Movies created"))
