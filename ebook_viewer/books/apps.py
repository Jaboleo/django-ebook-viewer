from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'
    fields = ('title', 'author_sort')