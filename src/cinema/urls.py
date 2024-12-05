from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import UserViewSet, MovieViewSet, UserFavouriteMoviesView

app_name = 'cinema'

# Для фильмов и пользователей регистрируются пути
router = DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('movies', MovieViewSet, 'movies')

# Для избранных фильмов для пользователей регистрируется пути для методов
# get, чтобы показать все избранные фильмы
fav_list  = UserFavouriteMoviesView.as_view({'get': 'list'})
# get, post и delete для просмотра, добавления нового фильма в избранное и удаление из избранного
fav_movie = UserFavouriteMoviesView.as_view({'get': 'retrieve', 'post': 'post', 'delete': 'delete'})


urlpatterns = [
        # slug:user_pk и <slug:pk> нужны для получения id пользователя и избранного фильма
        path("v1/users/<slug:user_pk>/favourites/", fav_list, name="user-favourites-list"),
        path("v1/users/<slug:user_pk>/favourites/<slug:pk>", fav_movie, name="user-favourite-details"),
        path('v1/', include(router.urls)),
]
