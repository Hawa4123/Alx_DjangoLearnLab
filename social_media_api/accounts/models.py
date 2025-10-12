from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser
    and includes a 'following' field for following other users.
    """
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
        bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
