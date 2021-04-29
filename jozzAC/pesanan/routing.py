from django.urls import re_path
from .consumers import NumberConsumer

ws_urlpatterns = [
	re_path('ws/pesanan/(?P<id>\w+)/', NumberConsumer.as_asgi())
]