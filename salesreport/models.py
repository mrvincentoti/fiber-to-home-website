from django.contrib.auth.models import AbstractUser
from django.db import models

#Create your models here.
# class CustomUser(AbstractUser):
#     is_kam = models.BooleanField(default=False)
#     is_cso = models.BooleanField(default=False)
#     is_management = models.BooleanField(default=False)

# class Kam(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Cso(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Management(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)