from django.contrib import admin

# Register your models here.
from .models import Carousels

class CarouselsAdmin(admin.ModelAdmin):
    list_display = ['caption','description','image']

admin.site.register(Carousels,CarouselsAdmin)