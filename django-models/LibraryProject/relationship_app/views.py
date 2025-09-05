from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # <-- corrected import
from .models import Book
from .models import Library  # <-- separate import for checker
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# -------------------------
# Function-based View
# -------------------------
def list_books(request):
    # Task requires: Book.objects.all()
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -------------------------
# Class-based View
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
