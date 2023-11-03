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
    age = models.DateField(blank=True, null=True) 
    
    def __str__(self):
        return self.user.username

   
class Product(models.Model):
    pro_category = models.CharField(max_length=50, blank=True,null=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_time = models.CharField(max_length=20, blank=True,null=True)  # Add this field for time period
    is_active = models.BooleanField(default=True,null=True)  # Add this field to track product status
    tailor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tailored_products', null=True, blank=True)

    # tailor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tailored_products')


    def __str__(self):
        return self.name


# models.py

from django.db import models
from django.conf import settings
class Measurement(models.Model):
    bust = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    shoulder_width = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fabric_type = models.CharField(max_length=255,null=True, blank=True)
    color = models.CharField(max_length=255,null=True, blank=True)
    reference_images = models.ImageField(upload_to='fabric_reference_images/', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='measurements')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'Measurement Entry {self.id}'
