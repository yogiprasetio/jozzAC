from django.db import models
from django.conf import settings
from django.utils.text import slugify

from product.models import ProductModel
from client.models import ClientModel

from collections import OrderedDict

# Create your models here.
    

      
class InvoiceModel(models.Model):
    """
    Description: Model Description
    """
    statusChoise = [
    ('LUNAS','LUNAS'),
    ('BELUM', 'BELUM LUNAS'),
    ]

    Invoice            = models.CharField(max_length=20, blank=True, verbose_name='Nomor Invoice')
    statusPembayaran    = models.CharField(choices=statusChoise, max_length=20, default='BELUM')
    Keterangan          = models.TextField()
    tanggal			    = models.DateField(auto_now=True, editable=False, verbose_name='Tanggal')
    totalInvoice	    = models.PositiveIntegerField(default=0, verbose_name='Total Pembayaran')
    slug_Invoice	    = models.SlugField()

    class Meta:
        verbose_name='Invoice'
        verbose_name_plural='Invoice'


    def save(self):
        # self.total	= self.jumlah_Ac * int(self.product.hargaProduct)
        super().save()
        if self.slug_Invoice == "":

            self.kwitansi       = f"INV/{str(self.id).zfill(4)}/{write_roman(self.tanggal.month)}/{self.tanggal.year}".upper()

            self.slug_Invoice	= slugify(f"{self.kwitansi}")

            self.save()

    def __str__(self):
    	return f"{self.kwitansi}"


class Job_OrderModel(models.Model):

    nomor_jo        = models.CharField(max_length=20, blank=True, verbose_name='NOMOR JO')
    product         = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name='productJO')
    client          = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, related_name='clientJO')
    invoice         = models.ForeignKey(InvoiceModel, on_delete=models.SET_NULL, related_name='invoiceJO', null=True, blank=True)
    jumlah_Ac       = models.PositiveIntegerField()
    total           = models.PositiveIntegerField()
    tgl_input       = models.DateField(auto_now=True)
    slugJO          = models.SlugField()

    def save(self):
        # self.total    = self.jumlah_Ac * int(self.product.hargaProduct)
        super().save()
        if self.slugJO == "":

            self.nomor_jo       = f"{str(self.id).zfill(4)}/JO/{write_roman(self.tgl_input.month)}/{self.tgl_input.year}".upper()

            self.slug_Pesanan   = slugify(f"{self.nomor_jo}")

            self.save()


    class Meta:
        verbose_name = "Job Order"
        verbose_name_plural = "Job Order"

    def __str__(self):
        return self.nomor_jo


class approvalModel(models.Model):
    statusChoice        = [
        ('SELESAI','SELESAI'),
        ('PENDING','PENDING'),
        ('CANCEL','CANCEL'),
    ]

    invoice             = models.OneToOneField(InvoiceModel, on_delete=models.DO_NOTHING, related_name='ApprovPesanan')
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

    no_pembayaran       = models.CharField(max_length=30, verbose_name='Nomor Pembayaran')
    tgl_input           = models.DateField(auto_now=True, verbose_name='Tanggal Input')
    invoice             = models.ForeignKey(InvoiceModel, on_delete=models.DO_NOTHING, related_name='payment')
    admin               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='admin')
    jumlah              = models.PositiveIntegerField(default=0, verbose_name='Jumlah Pembayaran')
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