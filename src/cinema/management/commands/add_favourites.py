"""
Команда добавляет избранные фильмы пользователям
"""
from django.core.management import BaseCommand
from django.db import transaction

from cinema.models import Movie, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Adding favourite movies to users")

            movie1 = Movie.objects.get(name="Very epic movie")

            movie2 = Movie.objects.get(name="Very epic movie 2:electric boogaloo")

            movie3 = Movie.objects.get(name="Disney Fantasy")

            movie4 = Movie.objects.get(name="Scarface")

            user1 = User.objects.get(first_name="Quentin")
            user2 = User.objects.get(first_name="David")

            user1.favourites.add(movie1)
            user1.favourites.add(movie2)
            user1.save()

            user2.favourites.add(movie4)
            user2.favourites.add(movie3)
            user2.save()

            self.stdout.write(self.style.SUCCESS("Favourite movies added to users"))
