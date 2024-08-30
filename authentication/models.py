from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 50 , unique=True)
    password = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 11 , unique=True, null=True)
    is_active = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    profile_img = models.ImageField(verbose_name="photo", upload_to='user/images/' ,default='default.jpg')
    birthdate = models.DateField(null = True)
    facebook_profile = models.URLField(null = True)
    country = models.CharField(max_length = 30 , null = True)
    last_login = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Register.objects.create(email=instance.email , password=instance.password , is_superuser=instance.is_superuser , is_active=instance.is_active ,first_name=instance.first_name , last_name=instance.last_name)