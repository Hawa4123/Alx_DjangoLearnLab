from django.db import models
from datetime import date

# Author model: stores the author name and optional birth date
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# Book model: stores book title, publication year, and author relationship
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
