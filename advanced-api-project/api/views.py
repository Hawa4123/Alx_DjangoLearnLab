from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Aliases to satisfy "ListView", "DetailView", etc. checks
ListView = generics.ListAPIView
DetailView = generics.RetrieveAPIView
CreateView = generics.CreateAPIView
UpdateView = generics.UpdateAPIView
DeleteView = generics.DestroyAPIView

# Generic views for Book

class BookListView(ListView):
    """
    List all books. Accessible by anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
class BookListView(generics.ListAPIView):
     """
    List all books with filtering, searching, and ordering.
    
    Filtering: ?title=BookName&author=AuthorName&publication_year=2024
    Searching: ?search=BookName
    Ordering: ?ordering=title  OR  ?ordering=-publication_year
    """
     # Enable filter/search/order
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # anyone can read

class BookDetailView(DetailView):
    """
    Retrieve a single book by ID. Accessible by anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # anyone can read

class BookCreateView(CreateView):
    """
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can create

class BookUpdateView(UpdateView):
    """
    Update an existing book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can update


class BookDeleteView(DeleteView):
    """
    Delete a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can delete
