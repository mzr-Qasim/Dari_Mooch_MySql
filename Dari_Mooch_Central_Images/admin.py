from django.contrib import admin
from .models import Central_Images
# Register your models here.
class Central_Images_Admin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Central_Images,Central_Images_Admin)