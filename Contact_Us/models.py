from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    firstname= models.CharField(max_length=60,null=True)
    lastname= models.CharField(max_length=60, null=True)
    email= models.CharField(max_length=60,null=True)
    phone= models.CharField(max_length=60,null=True)
    message= models.TextField(null=True)