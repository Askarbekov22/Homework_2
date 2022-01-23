from django.urls import path
from . import views
app_name='books'
urlpatterns = [
    path('books/', views.BooksListView.as_view(), name="book_all"),
    path('books/<int:id>/', views.BooksDetailView.as_view(), name="books_detail"),
    path('books/<int:id>/update/', views.BooksUpdateView.as_view(), name="book_update"),
    path('books/<int:id>/delete/', views.BooksDeleteView.as_view(), name="book_delete"),
    path('add-books/', views.BooksCreateView.as_view(), name='add_book'),
]

















