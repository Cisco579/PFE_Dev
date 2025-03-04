from django.contrib.auth.models import AbstractUser
from django.db import models

#model user's role before login
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('visitor', 'Visitor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='visitor')
