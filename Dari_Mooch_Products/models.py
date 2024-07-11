from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=60)
    category = models.CharField(max_length=60)
    price = models.IntegerField()
    price_off = models.IntegerField(null=True,blank=True)
    image = models.FileField(max_length=200, upload_to="products/",null=True)