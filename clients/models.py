from django.db import models
from django.db.models.signals import pre_save
import uuid
# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    token=models.UUIDField(default=uuid.uuid4,editable=False,null=False,blank=False)
    
    def __str__(self):
        return self.name
        
    class ReadonlyMeta:
        readonly = ["token"]