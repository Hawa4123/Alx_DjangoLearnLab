from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer with validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Validate that publication_year is not in the future
    def validate_publication_year(self, value):
        if value and value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'books']
