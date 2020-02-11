from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

from .models import Books, BooksAuthorsLink, Authors
from .serializers import BooksSerializer, AuthorsSerializer

class BooksList(generics.ListCreateAPIView):
    # queryset = Books.objects.all()[:999]
    # queryset = Books.objects.all().prefetch_related('authors','series','rating','tags')[:999]

    queryset = []
    i = 0
    while True:
        instance = Books.objects.all().prefetch_related('authors','series','rating','tags')[i*999:(i+1)*999]
        queryset += instance
        if len(instance) < 999:
            break
        i += 1
    print(len(queryset))
    serializer_class = BooksSerializer


