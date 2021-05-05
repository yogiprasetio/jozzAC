from django.contrib import admin
from .models import SPKModel

# Register your models here.
class SPKAdmin(admin.ModelAdmin):
    '''
        Admin View for SPK
    '''
    list_display = ('no_SPK', 'tgl_input', 'teknisi', 'pesanan', 'status')
    list_filter = ('tgl_input', 'teknisi')


    readonly_fields = ('tgl_input', 'slug_SPK')
    search_fields = ('no_SPK',)

admin.site.register(SPKModel, SPKAdmin)