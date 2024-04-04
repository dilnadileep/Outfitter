from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.conf import settings
from datetime import datetime


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
    ad1 = models.CharField(max_length=255, null=True, blank=True)
    ad2 = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=15, null=True, blank=True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Measurement Entry {self.id}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
    mesurment = models.ForeignKey(Measurement, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False,null=True)  # Add this field to track product status
    status = models.BooleanField(default=True,null=True)  # Add this field to track product status
    order_date = models.DateTimeField(default=datetime.now, blank=True)  # Add the order_date field
    pay_status = models.BooleanField(default=False,null=True)  # Add this field to track product status





from datetime import datetime

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_datetime = models.DateTimeField(default=datetime.now, blank=True)
    payee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ), default='Pending')
   
   

class OrderStatus(models.Model):
    ORDER_STATUSES = (
        ('Out for Delivery', 'Out for Delivery'),
        ('Quality Check', 'Quality Check'),
        ('Assembly', 'Assembly'),
        ('Cutting', 'Cutting'),
        ('Fabric dyeing', 'Fabric dyeing'),
        ('Pattern Making', 'Pattern Making'),
        ('Measurement and Consultation', 'Measurement and Consultation'),

    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=ORDER_STATUSES, default='Measurement and Consultation')

    def __str__(self):
        return f"Order ID: {self.order.id} - Status: {self.status}"


from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()

# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to='media/', blank=True, null=True)  # Field to store media
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    media = models.FileField(upload_to='media/', blank=True, null=True)  # Field to store media
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    
class c_Product(models.Model):
    c_category = models.CharField(max_length=50, blank=True, null=True)
    t_category = models.CharField(max_length=50, blank=True, null=True)    
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='c_products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    delivery_time = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)  


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(c_Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L')], default='M')
    tailor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tailor_cart', blank=True, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    is_active = models.BooleanField(default=False,null=False)  # Add this field to track product status
    is_rejected = models.BooleanField(default=False,null=False)  # Add this field to track if the order is rejected by tailor
    is_customized = models.BooleanField(default=False,null=False)  # Add this field to track if the order is rejected by tailor
    pay_status = models.BooleanField(default=False,null=True)  # Add this field to track product status
    customization_added = models.BooleanField(default=False,null=True)  # Add this field to track product status


    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.product.description}"


class cart_design(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name='designs')
    neck_design = models.ImageField(upload_to='designs/', null=True, blank=True)
    back_design = models.ImageField(upload_to='designs/', null=True, blank=True)
    sleev_design = models.ImageField(upload_to='designs/', null=True, blank=True)
    lining_design = models.ImageField(upload_to='designs/', null=True, blank=True)
    additional_info = models.TextField(verbose_name="Additional Information", blank=True, null=True, help_text="Add any additional information here.")

    def __str__(self):
        return f"Designs for Order #{self.order.id}"


class Payment2(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_datetime = models.DateTimeField(default=datetime.now, blank=True)
    payee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ), default='Pending')
   
   