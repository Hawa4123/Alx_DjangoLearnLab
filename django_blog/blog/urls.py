from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
=======
from django.contrib.auth import views as auth_views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Post CRUD
     path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path("profile/", views.profile, name="profile"),
     path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),

    # Update an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),

    # Delete a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Optional: simple auth endpoints if not defined elsewhere
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # if you have register view in views.py
>>>>>>> 01453906fcb7d027b6b6a570e403a8fd0ee37c7b
]
from .views import search_posts

urlpatterns += [
    path("search/", search_posts, name="search-posts"),
]
from .views import PostByTagListView

urlpatterns += [
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
]
