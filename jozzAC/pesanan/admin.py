from django.contrib import admin
from .models import InvoiceModel, approvalModel, pembayaranModel, Job_OrderModel

# Register your models here.

class JOAdmin(admin.TabularInline):

    model = Job_OrderModel

class InvoiceAdmin(admin.ModelAdmin):
    '''
        Admin View for Pesanan
    '''
    inlines = [Job_OrderModel]
    list_display = ('tanggal', 'kwitansi','tanggal', 'total',)
    list_filter = ('tanggal',)

    readonly_fields = ('kwitansi', 'slug_Pesanan', 'tanggal')
    search_fields = ('kwitansi', )
admin.site.register(InvoiceModel, InvoiceAdmin)

class ApprovalAdmin(admin.ModelAdmin):
    '''
        Admin View for Pesanan
    '''
    # model = [PesananModel]
    list_display = ('pesanan','approve', 'tgl_approve',)
    list_filter = ('tgl_approve',)

    readonly_fields = ('tgl_approve', 'slug_Approv')
    search_fields = ('pesanan', )
admin.site.register(approvalModel, ApprovalAdmin)

class PembayaranAdmin(admin.ModelAdmin):
    '''
        Admin View for Pesanan
    '''
    list_display = ('tgl_input', 'no_pembayaran','pesanan', 'jumlah', 'tgl_pembayaran')
    list_filter = ('no_pembayaran',)

    readonly_fields = ('tgl_input', 'slug_pembayaran')
    search_fields = ('no_pembayaran', )
admin.site.register(pembayaranModel, PembayaranAdmin)