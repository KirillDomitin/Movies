from django.core.paginator import Paginator
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.api.v1.mixins import MoviesApiMixin


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        page = self.request.GET.get('page', 1)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_films = list(paginator.get_page(page).object_list.values())
        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': paginator.page(page).previous_page_number() if paginator.page(page).has_previous() else False,
            'next': paginator.page(page).next_page_number() if paginator.page(page).has_next() else False,
            'result': page_films
        }


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    pk_url_kwarg = "uuid"

    def get_context_data(self, **kwargs):
        result = {k: v for k, v in self.object.__dict__.items() if not k.startswith('_')}
        return result
