from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    '''
        Admin View for Account
    '''
    list_display = ('username', 'last_login')

    readonly_fields = ('last_login',)
    search_fields = ('username',)

admin.site.register(Account, AccountAdmin)