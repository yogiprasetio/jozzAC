from django.db import models
from django.conf import settings
from django.utils.text import slugify

from product.models import ProductModel
from client.models import ClientModel

from collections import OrderedDict

# Create your models here.
      
class PesananModel(models.Model):
    """
    Description: Model Description
    """
    kwitansi        = models.CharField(max_length=20, blank=True)
    product 		= models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name='produk')
    client          = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, verbose_name='Nama Client')
    jumlah_Ac		= models.PositiveIntegerField()
    tanggal			= models.DateField(auto_now=True, editable=False)
    total			= models.PositiveIntegerField(default=0)
    slug_Pesanan	= models.SlugField()

    class Meta:
        verbose_name='Pesanan'
        verbose_name_plural='Pesanan'

    def save(self):
        self.total	= self.jumlah_Ac * int(self.product.hargaProduct)
        super().save()
        if self.slug_Pesanan is "":

            self.kwitansi       = f"""INV/{str(self.id).zfill(4)}/
                                    {write_roman(self.tanggal.month)}/
                                    {self.tanggal.year}""".upper()

            self.slug_Pesanan	= slugify(f"{self.kwitansi}")

            self.save()

    def __str__(self):
    	return f"{self.kwitansi}"


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


class approvalModel(models.Model):

    statusChoice        = [
        ('SELESAI','SELESAI'),
        ('PANDING','PANDING'),
        ('CANCEL','CANCEL'),
    ]

    pesanan             = models.OneToOneField(PesananModel, on_delete=models.DO_NOTHING, related_name='pesanan')
    admin               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='adminApprov')
    teknisi             = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='teknisi', null=True, blank=True)
    keterangan          = models.TextField(null=True, blank=True)
    tgl_approve         = models.DateField(null=True, blank=True)
    tgl_pengerjaan      = models.DateField(null=True, blank=True)
    approve             = models.BooleanField(default=False)
    status              = models.CharField(max_length=10, choices=statusChoice, default='PANDING')


    class Meta:
        verbose_name = "Approval"
        verbose_name_plural = "Approval Pesanan"

    def __str__(self):
        return f"{self.pesanan}"
    