from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value and (value < 0 or value > 2100):
            raise serializers.ValidationError("Publication year must be between 0 and 2100.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # <-- nested relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'books']
