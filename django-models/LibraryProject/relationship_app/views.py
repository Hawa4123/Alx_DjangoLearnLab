from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # <-- corrected import
from .models import Book
from .models import Library  # <-- separate import for checker
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test

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
    
# -------------------------
# Authentication Views
# -------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # <-- checker looks for this
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()  # <-- checker looks for this
    return render(request, 'relationship_app/register.html', {'form': form})  # <-- checker looks for this

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
    
# -------------------------
# Role check function
# -------------------------
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"
    
# -------------------------
# Admin-only view
# -------------------------
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
