from rest_framework import serializers
from .models import Books, Authors, Series, CustomColumn1, Tags, Ratings

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('name',)

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('name',)

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('rating',)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name',)

class CustomColumn1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomColumn1
        fields = ('value',)

class BooksSerializer(serializers.ModelSerializer):
    authors = AuthorsSerializer(many=True, read_only=True)
    series = SeriesSerializer(read_only=True)
    rating = RatingsSerializer(read_only=True)
    tags = TagsSerializer(read_only=True)
    # genre = CustomColumn1Serializer(read_only=True)
    class Meta:
        model = Books
        fields = ( 'title','pubdate','authors','rating', 'series', 'series_index', 'tags')
        # fields = "__all__"

# class BooksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Books
#         fields = (
#     'title' ,
#     'sort' ,
#     'timestamp' ,
#     'pubdate',
#     'series_index' ,
#     'author_sort',
#     'isbn' ,
#     'lccn',
#     'path',
#     'flags' ,
#     'uuid' ,
#     'has_cover' ,
#     'last_modified' ,
#     'authors',
#     'series' ,
#     'rating' ,
#         )
        # fields = "__all__"


        



        