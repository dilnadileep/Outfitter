from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    
    # USERNAME_FIELD = 'email'
    username=models.CharField(max_length=32, blank=True,unique=True, null=True)
    email = models.EmailField(unique=True)
    is_customer=models.BooleanField('is_customer',default=False,null=True)
    is_tailor=models.BooleanField('is_tailor',default=False,null=True)
    REQUIRED_FIELDS = []
    


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username


from django.db import models
from django.contrib.auth.models import User

class Garment(models.Model):
    tailor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='garment_images/')  # Image field

    def __str__(self):
        return self.title

   