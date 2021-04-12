from django.db import models
from django.utils.text import slugify

# Create your models here.
class ClientModel(models.Model):
    """
    Description: Model Description
    """
    nama_Client 		= models.CharField(max_length=30)
    noTelp_Client		= models.CharField(max_length=15)
    email_Client		= models.EmailField()
    alamat_Client		= models.CharField(max_length=254)
    kecamatan_Client	= models.CharField(max_length=30)
    kelurahan_Client	= models.CharField(max_length=30)
    kodePos_Client		= models.CharField(max_length=30)
    kota_Client			= models.CharField(max_length=30, default='SURABAYA')
    slug_Client			= models.SlugField()

    def save(self):
    	super().save()
    	if self.slug_Client is "":
    		self.slug_Client = slugify(f"{self.id}_{self.nama_Client}_{self.noTelp_Client}")
    		self.save()

    def __str__(self):
    	return f"{self.id}-{self.nama_Client}"