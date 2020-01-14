from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

from .models import Books, BooksAuthorsLink, Authors
from .serializers import BooksSerializer, BooksAuthorsLinkSerializer, AuthorsSerializer

# Create your views here.
class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
