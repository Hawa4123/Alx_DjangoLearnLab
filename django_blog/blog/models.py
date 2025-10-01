from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)   # ✅ title
    content = models.TextField()               # ✅ content
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ author
    published_date = models.DateTimeField(default=timezone.now) # ✅ published_date

    def __str__(self):
        return self.title
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Create or update Profile when User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
