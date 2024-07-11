from django.contrib import admin

# Register your models here.

from .models import Contact_Us

class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','phone','message']

admin.site.register(Contact_Us,ContactAdmin)