from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = None
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=500)
    image = models.ImageField(upload_to=f'{settings.MEDIA_ROOT}/media/photos', default='media/default.png', blank=True, null=True)
    is_superuser = models.BooleanField(default=False, null=True, blank=True)
    is_doctor = models.BooleanField(default=False, null=True, blank=True)
    specialty = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.name
