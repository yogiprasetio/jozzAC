from django.urls import path

from .views import produkView

app_name = 'product'
urlpatterns = [
    path('', produkView.as_view(), name='produkView'),
]