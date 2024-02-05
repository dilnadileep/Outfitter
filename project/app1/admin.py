from django.contrib import admin
from .models import CustomUser,UserProfile,Product,Measurement,Order
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Measurement)
admin.site.register(Order)


from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Thread,ChatMessage

admin.site.register(ChatMessage)


class ChatMessage(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
