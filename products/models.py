from django.core.urlresolvers import reverse 
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class ProductManager (models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Product(models.Model):
    title  = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    objects = ProductManager()
    quantity = models.IntegerField(default=0)
    zip_Code = models.CharField(blank = True, max_length=6)
    address = models.CharField(default=False, max_length=60)
    date_created = models.DateTimeField(default=timezone.now)
    date_Update = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return (self.title)
    def get_absolute_url(self):
        return reverse("product_detail", kwargs = {"pk": self.pk})



class Variation(models.Model):
    product = models.ForeignKey(Product)
    title  = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    saleprice = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_price(self):
        if self.sale_price is None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

def product_post_reciever(sender, instance, created, *args, **kwargs):
        
    product = instance
    variations = product.variation_set.all
    varations = Variation.objects.filter(product=product)
    if variations.count() == 0:
        new_var = Variation()
        new_var.product = product
        new_var.title = "default"
        new_var.price = product.price
        new_var.save()
    print sender

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)






#Image rename function
def image_upload_to(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)

    return "product/%s/%s" %(slug, new_filename)

#product Image
class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload_to)
    

    def get_absolute_url(self):
        return self.product.title()

post_save.connect(product_post_reciever, sender=ProductManager)
