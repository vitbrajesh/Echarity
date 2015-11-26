from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class List_items1(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=60)
    quentity = models.IntegerField()
    zipcode = models.CharField(max_length=6)
    discription = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)
    expiry_date = models.DateTimeField(
            blank=True, null=True)
    address = models.CharField(max_length=200)            
   
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
