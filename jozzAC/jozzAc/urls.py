
from django.contrib import admin
from django.urls import path, include

from .views import dasboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls', namespace='product')),
    path('pesanan/', include('pesanan.urls', namespace='pesanan')),
    path('', dasboard, name='dasboard'),
]
