from django.contrib import admin
from .models import CustomUser,UserProfile,Product
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Product)

