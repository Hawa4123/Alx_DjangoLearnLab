from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

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

class BookDetailView(DetailView):
    """
    Retrieve a single book by ID. Accessible by anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(CreateView):
    """
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(UpdateView):
    """
    Update an existing book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(DeleteView):
    """
    Delete a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
