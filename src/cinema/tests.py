from django.db.models import Prefetch

from rest_framework.test import APITestCase
from rest_framework import status

from cinema.models import Movie, User

from cinema.serializers import MovieSerializer, UserFlatSerializer


class CinemaAPITest(APITestCase):
    fixtures = ['test_fixtures.json']

    def test_api_returns_users_list(self):
        url = '/cinema/v1/users/'
        response = self.client.get(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        users_list = response.json()

        queryset = User.objects.all()

        db_data = UserFlatSerializer(queryset, many=True).data

        # запрос напрямую идентичен тому, что возвращает API
        self.assertEqual(db_data, users_list)

    def test_api_returns_movies_list(self):
        url = '/cinema/v1/movies/'
        response = self.client.get(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movies_list = response.json()

        queryset = Movie.objects.all()

        db_data = MovieSerializer(queryset, many=True).data

        # запрос напрямую идентичен тому, что возвращает API
        self.assertEqual(db_data, movies_list)

    def test_api_returns_users_favourite_movies(self):
        url = '/cinema/v1/users/3/favourites/'
        response = self.client.get(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movies_list = response.json()

        # запрашиваем избранные фильмы пользователя с id = 3
        queryset = User.objects.get(id=3).favourites.all()

        db_data = MovieSerializer(queryset, many=True).data

        # запрос напрямую идентичен тому, что возвращает API
        self.assertEqual(db_data, movies_list)

    def test_api_adds_favourite_movie_to_user(self):
        url = '/cinema/v1/users/3/favourites/'
        response = self.client.get(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # сохраняем данные до добавления в список нового фильма
        old_movies_list = response.json()
        old_queryset = User.objects.get(id=3).favourites.all()
        old_db_data = MovieSerializer(old_queryset, many=True).data


        url = '/cinema/v1/users/3/favourites/3'
        response = self.client.post(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        new_movies_list = response.json()

        # запрашиваем избранные фильмы пользователя с id = 3
        queryset = User.objects.get(id=3).favourites.all()

        db_data = MovieSerializer(queryset, many=True).data


        # результаты до и после добавления различаются как от API
        self.assertNotEqual(old_movies_list, new_movies_list)
        self.assertTrue(len(new_movies_list) > len(old_movies_list))
        # так и от БД
        self.assertNotEqual(old_db_data, db_data)
        self.assertTrue(len(db_data) > len(old_db_data))

        # т.к. даные в БД и от API равны
        self.assertEqual(db_data, new_movies_list)
        # можно проверить, что в БД в списке избранных у пользователя есть фильм с id = 3
        self.assertTrue(User.objects.get(id=3).favourites.filter(id=3).exists())

    def test_api_delete_favourite_movie_from_user(self):
        url = '/cinema/v1/users/3/favourites/'
        response = self.client.get(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # сохраняем данные до удаления из списка фильма
        old_movies_list = response.json()
        old_queryset = User.objects.get(id=3).favourites.all()
        old_db_data = MovieSerializer(old_queryset, many=True).data


        url = '/cinema/v1/users/3/favourites/1'
        response = self.client.delete(url)

        # запрос должен возвращать статус ОК
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        new_movies_list = response.json()

        # запрашиваем избранные фильмы пользователя с id = 3
        queryset = User.objects.get(id=3).favourites.all()

        db_data = MovieSerializer(queryset, many=True).data


        # результаты до и после добавления различаются как от API
        self.assertNotEqual(old_movies_list, new_movies_list)
        self.assertTrue(len(old_movies_list) > len(new_movies_list))
        # так и от БД
        self.assertNotEqual(old_db_data, db_data)
        self.assertTrue(len(old_db_data) > len(db_data))

        # т.к. даные в БД и от API равны
        self.assertEqual(db_data, new_movies_list)
        # можно проверить, что в БД в списке избранных у пользователя есть фильм с id = 3
        self.assertFalse(User.objects.get(id=3).favourites.filter(id=1).exists())
