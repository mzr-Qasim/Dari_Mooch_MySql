from django.contrib import admin

# Register your models here.
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','price_off','image']

admin.site.register(Products,ProductAdmin)