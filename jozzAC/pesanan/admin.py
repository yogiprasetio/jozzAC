from django.contrib import admin
from .models import PesananModel

# Register your models here.
class PesananAdmin(admin.ModelAdmin):
    '''
        Admin View for Pesanan
    '''
    model = [PesananModel]
    list_display = ('kwitansi','tanggal', 'total')
    list_filter = ('tanggal',)

    readonly_fields = ('slug_Pesanan', 'total', 'tanggal')
    search_fields = ('kwitansi', )
admin.site.register(PesananModel, PesananAdmin)