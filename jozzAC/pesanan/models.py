from django.db import models
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
    product 		= models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    client          = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING)
    jumlah_Ac		= models.PositiveIntegerField()
    tanggal			= models.DateField(auto_now=True, editable=False)
    total			= models.PositiveIntegerField(default=0)
    slug_Pesanan	= models.SlugField()

    def save(self):
        self.total	= self.jumlah_Ac * int(self.product.hargaProduct)
        super().save()
        if self.slug_Pesanan is "":

            self.slug_Pesanan	= slugify(f"""INV_{str(self.id).zfill(4)}
                                            _{write_roman(self.tanggal.month)}
                                            _{self.tanggal.year}""")

            self.kwitansi       = f"""INV/{str(self.id).zfill(4)}/
                                    {write_roman(self.tanggal.month)}/
                                    {self.tanggal.year}""".upper()
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
    print("".join([a for a in change(num)]))
    return "IV"
