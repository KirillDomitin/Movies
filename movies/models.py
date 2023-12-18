"""Create your models here."""

import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    """Абстрактный класс для полей created и modified."""

    created_at = models.DateTimeField(_("created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated"), auto_now=True)

    class Meta:
        # Этот параметр указывает Django,
        # что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    """Абстрактный класс для поля id."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    """Модель для жанра."""

    name = models.TextField(_("name"))
    description = models.TextField(_("description"), null=True)

    class Meta:
        verbose_name = _("genre")
        verbose_name_plural = _("genres")
        db_table = 'content{}genre'.format('.')

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    """Модель для актера."""

    full_name = models.CharField(_("full name"), max_length=255, blank=False)

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
        db_table = 'content{}person'.format('.')

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):
    """Модель для фильма."""

    class FilmworkType(models.TextChoices):
        MOVIE = "movie", "фильм"
        TV_SHOW = "tv_show", "сериал"

    title = models.TextField(_("title"))
    description = models.TextField(_("description"), blank=True, null=True)
    file_path = models.TextField(_("file path"), blank=True, null=True)
    creation_date = models.DateField(
        _("creation date"), default=None, null=True, blank=True
    )
    rating = models.FloatField(
        _("rating"),
        null=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.CharField(
        _("type"), max_length=10, choices=FilmworkType.choices, default="movie"
    )
    genre = models.ManyToManyField(Genre, through="GenreFilmwork")
    person = models.ManyToManyField(Person, through="PersonFilmwork")

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме.
        # Это нужно указать в классе модели
        verbose_name = _("film")
        verbose_name_plural = _("films")
        db_table = 'content{}film_work'.format('.')

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    """Модель жанров фильма."""

    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created"), auto_now_add=True)

    class Meta:
        verbose_name = _("film genre")
        verbose_name_plural = _("film genres")
        db_table = 'content{}genre_film_work'.format('.')
        unique_together = (
            "film_work",
            "genre",
        )


class PersonFilmwork(UUIDMixin):
    """Модель актеров фильма."""

    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.TextField(_("role"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = _("film person")
        verbose_name_plural = _("film persons")
        db_table = 'content{}person_film_work'.format('.')
        unique_together = ("film_work", "person", "role")
