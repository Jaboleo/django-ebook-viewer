from rest_framework import serializers
from .models import Books, Authors, BooksAuthorsLink

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ["name"]

class BooksAuthorsLinkSerializer(serializers.ModelSerializer):
    names = serializers.RelatedField(source="author", read_only=True)
    class Meta:
        model = BooksAuthorsLink
        fields = ("names",)

class BooksSerializer(serializers.ModelSerializer):
    authors = BooksAuthorsLinkSerializer(source ="booksauthorslink_set")
    # books_series = BooksSeriesLinkSerializer(source = "BooksSeriesLink_set")
    class Meta:
        model = Books
        fields = ( 'title','authors',)

        



        