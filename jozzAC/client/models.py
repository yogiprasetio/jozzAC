from django.db import models
from django.utils.text import slugify

# Create your models here.
class ClientModel(models.Model):
    """
    Description: Model Description
    """
    nama_Client 		= models.CharField(max_length=30, verbose_name='Nama')
    noTelp_Client		= models.CharField(max_length=15, verbose_name='Phone')
    email_Client		= models.EmailField(verbose_name='Email')
    alamat_Client		= models.CharField(max_length=254, verbose_name='Alamat')
    kecamatan_Client	= models.CharField(max_length=30, null=True, verbose_name='Kecamatan')
    kelurahan_Client	= models.CharField(max_length=30, null=True, verbose_name='Kelurahan')
    kodePos_Client		= models.CharField(max_length=30, null=True, verbose_name='Kode Pos')
    kota_Client			= models.CharField(max_length=30, default='SURABAYA', null=True, verbose_name='Kota')
    slug_Client			= models.SlugField()

    class Meta:
        verbose_name='Client'

    def save(self):
    	super().save()
    	if self.slug_Client == "":
    		self.slug_Client = slugify(f"{self.id}_{self.nama_Client}_{self.noTelp_Client}")
    		self.save()

    def __str__(self):
    	return f"{self.id}-{self.nama_Client}"