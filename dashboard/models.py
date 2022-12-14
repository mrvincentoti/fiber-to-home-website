from distutils.command.upload import upload
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django_resized import ResizedImageField

from uuid import uuid4
from django.urls import reverse
import os

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    addressLine1 = models.CharField(null=True, blank=True, max_length=100)
    addressLine2 = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    province = models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(null=True, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=100)
    profileImage = ResizedImageField(
        size=[100, 100], quality=90, upload_to='profile_image')
    # ADD OTHER VARIABLES HERE

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Permissions
    is_kam = models.BooleanField(default=False)
    is_cso = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.email)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.is_kam is None:
            self.is_kam = False
        if self.is_cso is None:
            self.is_cso = False
        if self.is_management is None:
            self.is_management = False

        self.slug = slugify('{} {} {}'.format(
            self.user.first_name, self.user.last_name, self.user.email))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)


class Home(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=244444)
    image = models.ImageField(upload_to='images')


class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    duration = models.CharField(max_length=244444)
    quantity = models.CharField(max_length=244444)
    speed = models.CharField(max_length=244444)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = models.CharField(max_length=244444)

    def __str__(self):
        return self.name


class Faqs(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=244444)

    def __str__(self):
        return self.title

class Coverage(models.Model):

    coverage_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    status = models.IntegerField(max_length=100, default = 0)

    def __str__(self):
        return self.coverage_name
