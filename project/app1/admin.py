from django.contrib import admin
from .models import CustomUser,UserProfile
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(UserProfile)

from .models import Garment

class GarmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'tailor', 'description', 'image')  # Add 'image' to the list_display

admin.site.register(Garment, GarmentAdmin)