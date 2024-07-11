from django.db import models

# Create your models here.
class Carousels(models.Model):
    caption = models.CharField(max_length=60)
    description = models.TextField(max_length=60)
    category = models.CharField(max_length=60)
    image= models.FileField(max_length=200 , upload_to="carousels/", null=True)