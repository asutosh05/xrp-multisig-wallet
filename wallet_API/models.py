from django.db import models

# Create your models here.
class Wallet(models.Model):
    account_id= models.CharField(max_length=120,null=False,blank=False)
    master_seed=models.CharField(max_length=120,null=False,blank=False)
    master_seed_hex=models.CharField(max_length=120,null=True,blank=True)
    public_key=models.CharField(max_length=120,null=True,blank=True)
    public_key_hex=models.CharField(max_length=120,null=True,blank=True)
