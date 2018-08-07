from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
class Clients(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    token=models.CharField(max_length=120,null=False,blank=False)
    
    def __str__(self):
        return self.name
        
   