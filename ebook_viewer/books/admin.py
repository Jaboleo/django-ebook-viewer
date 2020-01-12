from django.contrib import admin

from .models import Books
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

admin.site.register(Books)