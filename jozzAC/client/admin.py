from django.contrib import admin
from .models import ClientModel

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    '''
        Admin View for Client
    '''
    model = [ClientModel]
    list_display = ('id', 'nama_Client', 'noTelp_Client', 'email_Client')
    list_filter = ('id',)

    readonly_fields = ('slug_Client',)
    search_fields = ('noTelp_Client', 'email_Client', 'nama_Client')

admin.site.register(ClientModel, ClientAdmin)