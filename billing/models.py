from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

User= settings.AUTH_USER_MODEL


class BillingProfile(models.Model):
    user = models.OneToOneField(User,null=True , blank=True)
    email = models.EmailField()
    active =models.BooleanField( default = True)
    update = models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.email

def user_created_receiver (sender, instance,created,*args, **kwargs): #user create vayesi biling profile banauna ko lagi
    if created and instance.email:
        BillingProfile.objets.get_or_create(user=instance ,email = instance.email)

post_save.connect(user_created_receiver , sender=User)
