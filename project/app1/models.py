# from django.contrib.auth.models import AbstractUser
# from django.db import models

# # Create your models here.
# class CustomUser(AbstractUser):
#     CUSTOMER = 1
#     ADMIN = 2
#     TAILOR = 3

#     ROLE_CHOICE = (
#         (CUSTOMER, 'customer'),
#         (ADMIN,'Admin'),
#         (TAILOR,'tailor')
#     )
#     username = None
#     USERNAME_FIELD  = 'email'
#     first_name = models.CharField(max_length=100, default='')
#     last_name   = models.CharField(max_length=100, default='')
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     # user_type = models.CharField(max_length=10, choices=ROLE_CHOICE, default='')
#     # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,default=CUSTOMER)
#     is_customer = models.BooleanField(default=False)
#     is_seller = models.BooleanField(default=False)
    
#     # REQUIRED_FIELDS = []
        
#     def _str_(self):
#         return self.first_name
    
    
    
    
    
    
    
    
    
#     #after table create
# #cmd  -- python manage.py makemigrations
# #        python manage.py migrate



from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     CUSTOMER = 1
#     ADMIN = 2
#     TAILOR = 3

#     ROLE_CHOICES = (
#         (CUSTOMER, 'Customer'),
#         (ADMIN, 'Admin'),
#         (TAILOR, 'Tailor')
#     )

#     #username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=100, default='')
#     last_name   = models.CharField(max_length=100, default='')
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     user_type = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
#     is_customer = models.BooleanField(default=False)
#     is_seller = models.BooleanField(default=False)

#     # Remove 'email' from REQUIRED_FIELDS
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.first_name

class CustomUser(AbstractUser):
    
    USERNAME_FIELD = 'email'
    username=models.CharField(max_length=32, blank=True,unique=True, null=True)
    email = models.EmailField(unique=True)
    is_customer=models.BooleanField('is_customer',default=False,null=True)
    is_tailor=models.BooleanField('is_tailor',default=False,null=True)
    REQUIRED_FIELDS = []
    