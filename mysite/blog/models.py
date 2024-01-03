from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,  BaseUserManager
from django.contrib.auth.backends import BaseBackend

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    edited_date = models.DateTimeField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return f'{self.title} by {self.author}'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.text} by {self.author}'
