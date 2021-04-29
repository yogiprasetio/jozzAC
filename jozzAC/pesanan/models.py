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
    kwitansi        = models.CharField(max_length=20, blank=True, verbose_name='Nomor Kwitansi')
    product 		= models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name='produk')
    client          = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, verbose_name='Nama Client', related_name='client')
    Keterangan      = models.TextField()
    jumlah_Ac		= models.PositiveIntegerField(verbose_name='Jumlah AC', null=True)
    tanggal			= models.DateField(auto_now=True, editable=False, verbose_name='Tanggal')
    total			= models.PositiveIntegerField(default=0, verbose_name='Total Pembayaran')
    slug_Pesanan	= models.SlugField()

    class Meta:
        verbose_name='Pesanan'
        verbose_name_plural='Pesanan'


    def save(self):
        # self.total	= self.jumlah_Ac * int(self.product.hargaProduct)
        super().save()
        if self.slug_Pesanan == "":

            self.kwitansi       = f"INV/{str(self.id).zfill(4)}/{write_roman(self.tanggal.month)}/{self.tanggal.year}".upper()

            self.slug_Pesanan	= slugify(f"{self.kwitansi}")

            self.save()

    def get_last_payment(self):
        print("Masuk")
        return self.payment.all().order_by('-id')[0]

    def __str__(self):
    	return f"{self.kwitansi}"


class approvalModel(models.Model):
    statusChoice        = [
        ('SELESAI','SELESAI'),
        ('PENDING','PENDING'),
        ('CANCEL','CANCEL'),
    ]

    pesanan             = models.OneToOneField(PesananModel, on_delete=models.DO_NOTHING, related_name='ApprovPesanan')
    admin               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='adminUser')
    approve             = models.BooleanField(default=False)
    tgl_approve         = models.DateField(null=True, blank=True, verbose_name='Tanggal Approval')
    keterangan          = models.TextField(null=True, blank=True, verbose_name='Keterangan')
    slug_Approv         = models.SlugField()

    class Meta:
        verbose_name = "Approval"
        verbose_name_plural = "Approval Pesanan"

    
    def save(self):
        self.slug_Approv = slugify(f"Approv-{self.pesanan}")
        super().save()

    def __str__(self):
        return f"{self.pesanan}"

class pembayaranModel(models.Model):
    """
    Description: Model Description
    """
    statusChoice        = [
        ('DP','UANG MUKA'),
        ('CICILAN','CICILAN'),
        ('LUNAS','LUNAS'),
    ]

    no_pembayaran       = models.CharField(max_length=30, verbose_name='Nomor Pembayaran')
    tgl_input           = models.DateField(auto_now=True, verbose_name='Tanggal Input')
    pesanan             = models.ForeignKey(PesananModel, on_delete=models.DO_NOTHING, related_name='payment')
    admin               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='admin')
    jumlah              = models.PositiveIntegerField(default=0, verbose_name='Jumlah Pembayaran')
    status              = models.CharField(choices=statusChoice, max_length=10)
    keterangan          = models.TextField()
    tgl_pembayaran      = models.DateField(verbose_name='Tanggal Pembayaran')
    slug_pembayaran     = models.SlugField()

    class Meta:
        verbose_name='Pembayaran'
        verbose_name_plural='Pembayaran'

    def get_payment(self):
        try:
            print("Masuk Payment")
            return self.payment_set.all().order_by('-id')[0]
        except IndexError:
            print('Error')

    def save(self):
        super().save()
        if self.slug_pembayaran == "":
            self.no_pembayaran       = f"{str(self.id).zfill(4)}/KM/{write_roman(self.tgl_input.month)}/{self.tgl_input.year}".upper()
            self.slug_pembayaran     = slugify(f"{self.no_pembayaran}")
            self.save()

    def __str__(self):
        return self.no_pembayaran

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