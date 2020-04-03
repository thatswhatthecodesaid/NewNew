from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=18)
    branch = models.CharField(max_length=50)
    admission_no = models.CharField(max_length=25)

