from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Driver(models.Model):
    user = models.ForeignKey(User)
    birthday = models.DateField(null=True)
    name  = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

# create user object to attach to driver object
def create_driver_user_callback(sender, instance, **kargs):
    driver, new = Driver.objects.get_or_create(user=instance)

post_save.connect(create_driver_user_callback, User)
