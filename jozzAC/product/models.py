from django.db import models
from django.utils.text import slugify

# Create your models here.
class ProductModel(models.Model):
    
    namaProduct	= models.CharField(max_length=30, null=False)
    keteranganProduct	= models.TextField()
    hargaProduct	= models.PositiveIntegerField()
    slugProduct	= models.SlugField(editable=False)

    def save(self):
    	self.slug = slugify(f"{self.namaProduct}")
    	super().save()

    def __str__(self):
    	return f"{self.namaProduct}"
