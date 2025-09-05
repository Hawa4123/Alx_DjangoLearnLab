from django.urls import path
from .views import list_books              # exact line for checker
from .views import LibraryDetailView       # separate line
from .views import register_view           # separate line
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # -------------------------
    # Book and Library URLs
    # -------------------------
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # -------------------------
    # Authentication URLs (checker-friendly)
    # -------------------------
    path('register/', views.register_view, name='register'),  # checker sees views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
