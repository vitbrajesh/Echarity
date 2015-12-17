from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
       user = models.ForeignKey(User, unique=False)
       docfile = models.FileField(upload_to='documents/%Y/%m/%d')
       firstname = models.CharField(max_length=200)
       lastname = models.CharField(max_length=200)
       address = models.CharField(max_length=500)
