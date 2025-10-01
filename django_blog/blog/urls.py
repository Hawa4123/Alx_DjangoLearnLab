from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
