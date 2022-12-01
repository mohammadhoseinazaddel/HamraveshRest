from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Author(models.Model):
    author_name = models.CharField(max_length=20, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.author_name


class ContainerApps(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.CharField(max_length=50, blank=False)
    envs = models.CharField(max_length=50, blank=False)
    command = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.name
