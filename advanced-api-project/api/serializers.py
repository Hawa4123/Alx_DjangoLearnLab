from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        """
        Example validation: ensure the book title is not empty.
        """
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value
class AuthorSerializer(serializers.ModelSerializer):
    # Include all books by this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books']
