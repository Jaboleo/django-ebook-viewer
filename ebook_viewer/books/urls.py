from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/<int:book_id>', views.BooksDetails.as_view())
]