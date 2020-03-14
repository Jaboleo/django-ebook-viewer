from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Books, BooksAuthorsLink, Authors
from .serializers import BooksSerializer, AuthorsSerializer, BookDetailsSerializer
from .filters import BookFilter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50

class BooksList(generics.ListAPIView):
    queryset = Books.objects.none()
    i = 0
    while True:
        instance = Books.objects.all().prefetch_related('authors','series','rating','tags')[i*999:(i+1)*999]
        queryset |= instance
        if len(instance) < 999:
            break
        i += 1
    print(f"Number of books in the database: {len(queryset)}")
    serializer_class = BooksSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BooksDetails(generics.ListAPIView):

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        queryset = Books.objects.filter(id=book_id).prefetch_related('authors','series','rating','tags')
        return queryset

    serializer_class = BookDetailsSerializer
