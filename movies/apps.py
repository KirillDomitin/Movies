"""Подключение приложений."""

from django.apps import AppConfig


class MoviesConfig(AppConfig):
    """Подключение приложения movies."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
    verbose_name = 'Фильмы'
