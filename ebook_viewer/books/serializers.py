from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('title','author_sort', 'path')