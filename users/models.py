from datetime import timezone
from random import random

from django.db import models

# Create your models here.
class Users(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
   # date_created=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=15)
    persona=models.CharField(max_length=20)

    def __str__(self):
        return self.username
