from django.db import models
from User.models import User


class Appointment(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(User, related_name='Doctor', on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=6)
    datetime = models.DateTimeField()
    is_done = models.BooleanField(default=False, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
