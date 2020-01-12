from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

from .models import Books, BooksAuthorsLink
from .serializers import BooksSerializer, BooksAuthorsLinkSerializer

# Create your views here.
class BooksList(generics.ListCreateAPIView):
    queryset = BooksAuthorsLink.objects.all()
    serializer_class = BooksAuthorsLinkSerializer
