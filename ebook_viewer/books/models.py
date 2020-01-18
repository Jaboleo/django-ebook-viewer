# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)
    link = models.TextField()

    class Meta:
        managed = False
        db_table = 'authors'
    
    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.TextField()
    sort = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)  # This field type is a guess.
    pubdate = models.TextField(blank=True, null=True)  # This field type is a guess.
    series_index = models.FloatField()
    author_sort = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    lccn = models.TextField(blank=True, null=True)
    path = models.TextField()
    flags = models.IntegerField()
    uuid = models.TextField(blank=True, null=True)
    has_cover = models.BooleanField(blank=True, null=True)
    last_modified = models.TextField()  # This field type is a guess.
    authors = models.ManyToManyField(Authors, through='BooksAuthorsLink')
    series = models.ManyToManyField("Series", through='BooksSeriesLink')
    rating = models.ManyToManyField("Ratings", through='BooksRatingsLink')

    class Meta:
        managed = False
        db_table = 'books'
    
    def __str__(self):
        return self.title


class BooksAuthorsLink(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='book')
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, db_column='author')

    class Meta:
        managed = False
        db_table = 'books_authors_link'

class Series(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'

class BooksCustomColumn1Link(models.Model):
    book = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_custom_column_1_link'


class BooksLanguagesLink(models.Model):
    book = models.IntegerField()
    lang_code = models.IntegerField()
    item_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_languages_link'


class BooksPluginData(models.Model):
    book = models.IntegerField()
    name = models.TextField()
    val = models.TextField()

    class Meta:
        managed = False
        db_table = 'books_plugin_data'


class BooksPublishersLink(models.Model):
    book = models.IntegerField()
    publisher = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_publishers_link'


class BooksRatingsLink(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE, db_column='book')
    rating = models.ForeignKey('Ratings', on_delete=models.CASCADE, db_column='rating')

    class Meta:
        managed = False
        db_table = 'books_ratings_link'


class BooksSeriesLink(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='book')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, db_column='series')

    class Meta:
        managed = False
        db_table = 'books_series_link'


class BooksTagsLink(models.Model):
    book = models.IntegerField()
    tag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_tags_link'


class Comments(models.Model):
    book = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class ConversionOptions(models.Model):
    format = models.TextField()
    book = models.IntegerField(blank=True, null=True)
    data = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'conversion_options'


class CustomColumn1(models.Model):
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'custom_column_1'


class CustomColumn2(models.Model):
    book = models.IntegerField(blank=True, null=True)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_column_2'


class CustomColumns(models.Model):
    label = models.TextField()
    name = models.TextField()
    datatype = models.TextField()
    mark_for_delete = models.BooleanField()
    editable = models.BooleanField()
    display = models.TextField()
    is_multiple = models.BooleanField()
    normalized = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'custom_columns'


class Data(models.Model):
    book = models.IntegerField()
    format = models.TextField()
    uncompressed_size = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'data'


class Feeds(models.Model):
    title = models.TextField()
    script = models.TextField()

    class Meta:
        managed = False
        db_table = 'feeds'


class Identifiers(models.Model):
    book = models.IntegerField()
    type = models.TextField()
    val = models.TextField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Languages(models.Model):
    lang_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'languages'


class LastReadPositions(models.Model):
    book = models.IntegerField()
    format = models.TextField()
    user = models.TextField()
    device = models.TextField()
    cfi = models.TextField()
    epoch = models.FloatField()
    pos_frac = models.FloatField()

    class Meta:
        managed = False
        db_table = 'last_read_positions'


class LibraryId(models.Model):
    uuid = models.TextField()

    class Meta:
        managed = False
        db_table = 'library_id'


class MetadataDirtied(models.Model):
    book = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metadata_dirtied'


class Preferences(models.Model):
    key = models.TextField()
    val = models.TextField()

    class Meta:
        managed = False
        db_table = 'preferences'


class Publishers(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishers'


class Ratings(models.Model):
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'




class Tags(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tags'
