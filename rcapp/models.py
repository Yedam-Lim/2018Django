from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    username = models.EmailField(unique=True, null=False, max_length=254)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Recordings(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE)
    datafile = models.FileField(upload_to='uploads/%Y/%m/%d/')
