<<<<<<< HEAD
from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),         # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),    # Add a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'), # Update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), # Delete a book
]

=======
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]
>>>>>>> 33ddc232c39db4425cc559cd88841abc6f6fb91d
