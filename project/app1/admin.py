from django.contrib import admin
from .models import CustomUser,UserProfile,Product,Measurement,Order
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Measurement)
admin.site.register(Order)

