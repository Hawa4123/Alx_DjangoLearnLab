from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView
from .views import admin_view   # add this line

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),  # checker sees views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("admin-view/", admin_view, name="admin_view"),
]
from django.urls import path
from .views import list_books, LibraryDetailView

