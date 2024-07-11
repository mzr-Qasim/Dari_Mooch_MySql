from django.db import models

# Create your models here.
class Central_Images(models.Model):
    image = models.FileField(max_length=200, upload_to="Dari-Mooch-Central-Images/",null=True)