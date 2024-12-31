from django.db import models
# Create your models here.

from django.contrib.auth.models import User

class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
