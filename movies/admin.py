"""Подключение моделей в панель администратора."""

from django.contrib import admin

from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    """Для выбора жанра при создании записи фильма."""

    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    """Для выбора актера при создании фильма."""

    model = PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Подключение модели Genre в панель администратора."""

    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name", "id")
    list_select_related = True


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Подключение модели Person в панель администратора."""

    list_display = ("full_name", "created_at", "updated_at")
    search_fields = ("full_name", "id")
    list_select_related = True


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    """Подключение модели Filmwork в панель администратора."""

    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    # Отображение полей в списке
    list_display = (
        "id",
        "title",
        "type",
        "creation_date",
        "rating",
        "created_at",
        "updated_at",
    )
    # Фильтрация в списке
    list_filter = ("type",)
    # Поиск по полям
    search_fields = ("title", "description", "id")
    list_select_related = True
