from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add-book', views.add_book),
    path('authors', views.authors),
    path('add-author', views.add_author),
    path('books/<int:book_id>', views.edit_book),
    path('authors/<int:author_id>', views.edit_author),
    path('add-author-to-book', views.add_author_to_book),
    path('add-book-to-author', views.add_book_to_author),
]

