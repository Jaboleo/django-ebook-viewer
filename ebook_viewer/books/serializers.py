from rest_framework import serializers
from .models import Books, BooksAuthorsLink, BooksSeriesLink

class BooksAuthorsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthorsLink
        fields =  ['author',]
        depth=1

class BooksSeriesLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSeriesLink
        fields = ('series',)
        depth = 1

class BooksSerializer(serializers.ModelSerializer):
    authors = BooksAuthorsLinkSerializer(source='booksauthorslink_set', many=True)
    series = BooksSeriesLinkSerializer(source='booksserieslink_set', many=True)
    class Meta:
        model = Books
        fields = ( 'title','authors','series')

        



        