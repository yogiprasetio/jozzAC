from django.contrib import admin
from .models import ProductModel

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for 
    '''
    model = [ProductModel]

    readonly_fields = ('slugProduct',)
    search_fields = ('namaProduct',)

admin.site.register(ProductModel, ProductAdmin)