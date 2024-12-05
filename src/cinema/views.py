from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from cinema.serializers import UserFlatSerializer, MovieSerializer
from cinema.models import User, Movie


class UserViewSet(ModelViewSet):
    """
    ViewSet для пользователей
    Отображает все поля, кроме избранных фильмов
    """
    queryset = User.objects.all()
    serializer_class = UserFlatSerializer


class MovieViewSet(ModelViewSet):
    """
    ViewSet для фильмов
    отображает все поля
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class UserFavouriteMoviesView(ModelViewSet):
    """
    ViewSet для избранных фильмов
    перегружает методы post и delete для изменения логики
    post - добавляет фильм в список избранных
    delete - удаляет фильм из списка избранных

    Используется сериализатор для фильмов
    """

    serializer_class = MovieSerializer

    def get_queryset(self):
        pk = self.kwargs.get("user_pk")
        if pk:
            user = get_object_or_404(User, id=pk)
            return user.favourites.all()
        return Response(status=status.HTTP_404_NOT_FOUND)

    def _validate_request(self):
        """
        Метод проверяет существование фильма и
        пользователя с id, переданными в запросе
        :return:
        """
        movie_pk = self.kwargs.get('pk')
        movie_exsists = False
        if movie_pk:
            movie_exsists = Movie.objects.filter(id=movie_pk).exists()

        user_pk = self.kwargs.get("user_pk")
        user_exsists = False
        if user_pk:
            user_exsists = User.objects.filter(id=user_pk).exists()

        return movie_exsists and user_exsists

    def post(self, request, *args, **kwargs):
        if self._validate_request():
            # Если фильм и пользователь существуют, то
            user = User.objects.get(id=self.kwargs.get("user_pk"))
            # добавляем в список избранных фильм c id из запроса
            user.favourites.add(self.kwargs.get("pk"))
            user.save()

            serializer = MovieSerializer(user.favourites.all(), many=True)
            # возвращаем новый список избранных фильмов
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if self._validate_request():
            # Если фильм и пользователь существуют
            user = User.objects.get(id=self.kwargs.get("user_pk"))
            # и фильм есть в списке избранных у пользователя
            if user.favourites.filter(id=self.kwargs.get("pk")).exists():
                # убираем фильм из списка
                user.favourites.remove(self.kwargs.get("pk"))
                user.save()

                serializer = MovieSerializer(user.favourites.all(), many=True)
                # возвращаем новый список избранных фильмов
                return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)
