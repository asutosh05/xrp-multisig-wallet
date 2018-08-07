from django.db import models

# Create your models here.
class Wallet(models.Model):
    address= models.CharField(max_length=120,null=False,blank=False)
    secretKey=models.CharField(max_length=120,null=False,blank=False)
