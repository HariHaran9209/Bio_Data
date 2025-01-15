from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserData(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userdata_set',  # Changed related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userdata_permissions',  # Changed related_name to avoid conflict
        blank=True
    )

class BioData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s BioData"