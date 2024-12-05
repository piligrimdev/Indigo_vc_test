from django.contrib import admin

from cinema.models import Movie, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = "first_name",


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = "name",
