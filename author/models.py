from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=40, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self) -> str:
        return self.name