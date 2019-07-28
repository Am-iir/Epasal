import random
import os
from django.db import models
from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3912023165316663)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)


class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)  #Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank =True , unique= True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank =True)

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug= self.slug)
        return reverse("detail" , kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

def product_pre_save_receiver(sender , instance , *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver , sender= Product)




