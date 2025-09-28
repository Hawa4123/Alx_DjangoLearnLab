from django.contrib import admin
from .models import Author, Book

# Register Author and Book for admin interface
admin.site.register(Author)
admin.site.register(Book)
