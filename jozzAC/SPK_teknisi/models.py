from django.db import models
from pesanan.models import approvalModel, InvoiceModel
from django.conf import settings
from django.utils.text import slugify

from collections import OrderedDict

# Create your models here.

class SPKModel(models.Model):
    """
    Description: Model Description
    """
    statusChoice        = [
        ('PENDING','ON PROGRESS'),
        ('CANCEL','CANCEL'),
        ('SELESAI','SELESAI'),
    ]

    no_SPK			= models.CharField(max_length=30, verbose_name='Nomor SPK', blank=True)
    tgl_input		= models.DateField(auto_now=True, verbose_name='Tanggal Input')
    teknisi			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='teknisiUser', verbose_name='Teknisi')
    pesanan		    = models.OneToOneField(InvoiceModel, related_name='SPK', on_delete=models.DO_NOTHING, verbose_name='Kwitansi')
    tgl_pengerjaan	= models.DateField(verbose_name='Tanggal Pengerjaan')
    keterangan		= models.TextField(verbose_name='Keterangan')
    status			= models.CharField(choices=statusChoice, max_length=10, default='PENDING')
    slug_SPK		= models.SlugField()

    class Meta:
        verbose_name='Surat Perintah Kerja'
        verbose_name_plural='Surat Perintah Kerja'

    def save(self):
    	super().save()
    	if self.slug_SPK == "":
    		self.no_SPK       	= f"SPK/{str(self.id).zfill(4)}/{write_roman(self.tgl_input.month)}/{self.tgl_input.year}".upper()
    		self.slug_SPK		= slugify(f"{self.no_SPK}")
    		self.save()

    def __str__(self):
    	return self.no_SPK

def write_roman(num):
    def change(num):
        roman = OrderedDict()
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in change(num)])