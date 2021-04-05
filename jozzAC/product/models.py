from django.db import models

# Create your models here.
class Model(models.Model):
    
    name_Product = models.CharField(max_length=30, null=False)
    desc_Product = models.TextField()
    # price_Product = models.
