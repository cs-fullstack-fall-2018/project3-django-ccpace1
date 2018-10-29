from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

    def __str__(self):
        return self.username

class UserSetup(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.name