from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse

from movies.models import Filmwork


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self, queryset=None):
        queryset = Filmwork.objects.order_by('id').annotate(
            genres=ArrayAgg('genre__name', distinct=True),
            actors=ArrayAgg(
                'person__full_name',
                filter=Q(person__personfilmwork__role='actor'),
                distinct=True
            ),
            writers=ArrayAgg(
                'person__full_name',
                filter=Q(person__personfilmwork__role='writer'),
                distinct=True
            ),
            directors=ArrayAgg(
                'person__full_name',
                filter=Q(person__personfilmwork__role='director'),
                distinct=True
            ),
        )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        json_params = {"indent": 4}
        return JsonResponse(context, json_dumps_params=json_params)
