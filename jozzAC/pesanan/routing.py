from django.urls import re_path
from .consumers import PesananConsumer

ws_urlpatterns = [
	re_path(r'^pesanan/admin/tracking/(?P<id>\w+)$', PesananConsumer.as_asgi())
]