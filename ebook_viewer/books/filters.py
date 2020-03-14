from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Books

class BookFilter(rest_framework.FilterSet):
    title = rest_framework.CharFilter(field_name="title", lookup_expr='contains')
    authors = rest_framework.CharFilter(field_name="authors__name", lookup_expr='contains')
    genre = rest_framework.CharFilter(field_name="genre__value", lookup_expr='contains')
    tag = rest_framework.CharFilter(field_name="tags__name", lookup_expr='contains')
    series = rest_framework.CharFilter(field_name="series__name", lookup_expr='contains')

    class Meta:
        model = Books
        fields = ['title', 'authors', 'genre', 'tag', 'series']