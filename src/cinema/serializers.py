"""
Сериализаторы для моделей User и Movie
"""
from rest_framework.serializers import ModelSerializer

from cinema.models import User, Movie


class MovieSerializer(ModelSerializer):
    """
    Сериализатор для фильмов
    Отображает все поля
    """
    class Meta:
        model = Movie
        fields = '__all__'


class UserFlatSerializer(ModelSerializer):
    """
    Сериализатор для пользователей
    Отображает все поля, кроме избранных фильмов
    """
    class Meta:
        model = User
        fields = 'id', 'first_name', 'second_name', 'birthday'
