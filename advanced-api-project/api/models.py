from django.db import models

# Author model: Represents a book author
class Author(models.Model):
    name = models.CharField(max_length=255)  # Store author's name

    def __str__(self):
        return self.name


# Book model: Represents books written by authors
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author, 
        related_name="books",   # Enables reverse lookup: author.books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
