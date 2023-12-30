from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

status=[("PENDING ","pending"),("PROCESSING","Processing"),("SHIPPED","Shipped")]

class Packages(models.Model):
    name=models.CharField(max_length=200)
    status=models.CharField(max_length=50,choices=status,default='pending')