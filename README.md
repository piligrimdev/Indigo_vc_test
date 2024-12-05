# Тестовое задание для INDIGO VC

## Установка и запуск

Для работы с проектом необходим `Python` версии `3.12` или новее.

1) Клонируйте git репозиторий на ваш компьютер
```commandline
git clone <адрес репозитория>
```
2) Активируйте виртуальное окружение в корне проекта:
```commandline
pip install virtualenv
python -m virtualenv venv 
.\venv\Scripts\activate 
```
3) Установите `poetry` в вашем виртуальном окружении
```commandline
python -m pip install poetry
```
4) Установите зависимости
```commandline
python -m poetry install
```
5) Выполните миграции
```commandline
cd src
python manage.py migrate
```
6) Создайте пользователя для админ-панели
```commandline
python manage.py createsuperuser      
```
7) Заполните бд данными
```commandline
python manage.py populate_movies
python manage.py populate_users
python manage.py add_favourites
```
Здесь `populate_movies` создает фильмы, `populate_users` - пользователей, а `add_favourites` добавляет в список избранных фильмы пользователям

8) Запустите сервер
```commandline
python manage.py runserver
```
## Как с этим работать?

* Для начала можете посмотреть, какие существуют фильмы, пользователи и какие фильмы пользователи добавили в избранное в админ панели: <br>
  `<локальный адрес сервера>/admin/cinema/`
* После, можете отправить `GET` запрос по адресам:
  * `<локальный адрес сервера>/cinema/v1/users`
  * `<локальный адрес сервера>/cinema/v1/movies`
  * `<локальный адрес сервера>/cinema/v1/users/<id пользователя>/favourites/`
  * `<локальный адрес сервера>/cinema/v1/users/<id пользователя>/favourites/<id фильма>`
* Можете сверить `json`-ответ (или ответ на DRF странице) с данными из админ-панели. <br>
Можно заметить, что по запросу `cinema/v1/users/<id пользователя>/favourites/` в ответе приходят фильмы из списка избранного конкретного пользователя.
* C пользователями и фильмами можно проводить CRUD-операции соотвествующими HTTP-запросами. 
* Можно отправить `POST` запрос вида: <br>
  `<локальный адрес сервера>/cinema/v1/users/<id пользователя>/favourites/<id фильма>` <br>
  Если фильма с указанным id в списке не было, он появится в списке избранного.
* Можно отправить `DELETE` запрос вида: <br>
  `<локальный адрес сервера>/cinema/v1/users/<id пользователя>/favourites/<id фильма>` <br>
  Если фильм с указанным id был в списке, он пропадет из списка.
* Также, можете запустить юнит-тесты, которые проверяют данные, полученные от API с запросом к базе данных напрямую: <br>
  `python manage.py test`