from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_1, name="book"),
    path('books/<int:id>/', views.book_2, name="books"),
    path('books/<int:id>/update/', views.book_update, name="book_update"),
    path('books/<int:id>/delete/', views.book_delete, name="book_delete"),
    path('add-books/', views.add_book, name='add_book'),
]





