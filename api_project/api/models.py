from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
>>>>>>> efee385d6c8f7a33a3a8e8e44a97537e13aecb57
