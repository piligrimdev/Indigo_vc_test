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

8) Создайте файл `.env` в корне проекта
    1) В `.env` вставьте шаблон из файла `.env_template`
    2) Для `DJANGO_SECRET` установите секретную строку на ваше усмотрение
    3) Для `DEBUG` установите значение `1`, если вам необходимо работать в режиме дебага и `0`, если нет.

9) Запустите сервер
```commandline
python manage.py runserver
```
