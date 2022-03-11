from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class martdb(models.Model):
    name=models.CharField(max_length=200,null=True,blank=False)
    description=models.CharField(max_length=200,null=True,blank=False)
    photo= models.ImageField(upload_to='image',default=0)
    
class productdb(models.Model):
    productname=models.CharField(max_length=200,null=True,blank=False)
    category=models.CharField(max_length=200,null=True,blank=False)
    weight=models.IntegerField(null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
    photo= models.ImageField(upload_to='image',default=0)


