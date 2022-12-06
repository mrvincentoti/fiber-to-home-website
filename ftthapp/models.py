from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.TextField()


class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.TextField()


class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.TextField()
    quantity = models.TextField()
    speed = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name


class Faqs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
