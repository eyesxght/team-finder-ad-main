from django.core.paginator import Paginator

from .constants import PAGINATE_BY


def get_paginated_queryset(queryset, request, per_page=PAGINATE_BY):
    """Вспомогательная функция для пагинации."""
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
