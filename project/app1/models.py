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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    delivery_time = models.CharField(max_length=20, blank=True,null=True)  # Add this field for time period
    is_active = models.BooleanField(default=True,null=True)  # Add this field to track product status
    #tailor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tailored_products', null=True, blank=True)



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
    fabric_type = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    style_design = models.CharField(max_length=255, null=True, blank=True)
    neck_design = models.CharField(max_length=255, null=True, blank=True)
    back_design = models.CharField(max_length=255, null=True, blank=True)
    sleev_design = models.CharField(max_length=255, null=True, blank=True)
    lining_design = models.CharField(max_length=255, null=True, blank=True)
    work_design = models.CharField(max_length=255, null=True, blank=True)
    additional_info = models.TextField(verbose_name="Additional Information",blank=True, null=True, help_text="Add any additional information here.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f'Measurement Entry {self.id}'



class Order(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
        customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
        mesurment = models.ForeignKey(Measurement, on_delete=models.CASCADE, null=True, blank=True)
        is_active = models.BooleanField(default=False,null=True)  # Add this field to track product status

