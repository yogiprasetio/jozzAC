from django.db import models
from django.utils.text import slugify
from product.models import ProductModel

# Create your models here.
class PesananModel(models.Model):
    """
    Description: Model Description
    """
    product 		= models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    nama			= models.CharField(max_length=20)
    jumlah_Ac		= models.PositiveIntegerField()
    alamat			= models.TextField(null=False)
    no_Telp			= models.CharField(max_length=15)
    tanggal			= models.DateField(auto_now=True, editable=False)
    total			= models.PositiveIntegerField(default=0)
    slug_Pesanan	= models.SlugField()

    def save(self):
    	self.total			= self.jumlah_Ac * int(self.product.hargaProduct)
    	super().save()
    	if self.slug_Pesanan is "":
    		print("Slug : ", self.slug_Pesanan)
	    	self.slug_Pesanan	= slugify(f"{self.id} - {self.nama}")
	    	self.save()

    def __str__(self):
    	return f"{self.id} - {self.nama} - {self.tanggal}"
