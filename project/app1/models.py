from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    USERNAME_FIELD = 'email'
    username=models.CharField(max_length=32, blank=True,unique=True, null=True)
    email = models.EmailField(unique=True)
    is_customer=models.BooleanField('is_customer',default=False,null=True)
    is_tailor=models.BooleanField('is_tailor',default=False,null=True)
    REQUIRED_FIELDS = []
    
    
     #cmd   python manage.py makemigrations
     #      python manage.py migrate