from rest_framework import serializers
from .models import Books, Authors, BooksAuthorsLink


class BooksAuthorsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthorsLink
        fields = '__all__'
        depth = 1

class BooksSerializer(serializers.ModelSerializer):
    group_set = BooksAuthorsLinkSerializer()
    class Meta:
        model = Books
        fields = ('title', 'group_set')
        depth = 2
        



        