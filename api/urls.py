from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Set up router for CRUD
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # List-only endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # CRUD endpoints via ViewSet + Router
    path('', include(router.urls)),
]
