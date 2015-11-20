from django.db import models
from django.utils import timezone


class Donatable_item(models.Model):
    #product = models.ForeignKey('auth.User')
    title = models.CharField(max_length=60)
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=150)
    photo = models.ImageField(upload_to='images', blank=True)
    zip_Code = models.CharField(max_length=6)
    address = models.CharField(max_length=60)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_Update = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
      
    def Update(self):
        self.date_Update = timezone.now()
        self.save()

    def __str__(self):
        return self.title
