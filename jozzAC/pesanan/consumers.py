from channels.generic.websocket import WebsocketConsumer
import json
from django.core import serializers
from .models import PesananModel

class NumberConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		data = serializers.serialize("json", PesananModel.objects.get(id=self.scope['url_route']['kwargs']['id']))
		print(data)
		self.send(json.dumps({data}))