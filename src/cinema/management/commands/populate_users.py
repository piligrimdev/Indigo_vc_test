"""
Заполняет таблицу с пользователями
"""

from django.core.management import BaseCommand
from django.db import transaction

from cinema.models import User

import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Creating users")

            tarantino, flag = User.objects.get_or_create(
               first_name="Quentin", second_name="Tarantino",
               birthday=datetime.date(year=1963, month=3, day=27)
            )

            ritchie, flag = User.objects.get_or_create(
               first_name="Guy", second_name="Ritchie",
               birthday=datetime.date(year=1968, month=9, day=10)
            )

            lynch, flag = User.objects.get_or_create(
               first_name="David", second_name="Lynch",
               birthday=datetime.date(year=1946, month=1, day=20)
            )

            baby, flag = User.objects.get_or_create(
                first_name="Little", second_name="Baby",
                birthday=datetime.date(year=2024, month=1, day=1)
            )

            self.stdout.write(self.style.SUCCESS("Users created"))
