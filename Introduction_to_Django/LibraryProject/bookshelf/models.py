from django.db import models

# 1️⃣ Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

# 2️⃣ Author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

# 3️⃣ Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.city}"
