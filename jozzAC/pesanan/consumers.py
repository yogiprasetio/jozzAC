from channels.consumer import AsyncConsumer
import asyncio
import json
from channels.db import database_sync_to_async
from django.core import serializers
from .models import PesananModel

class PesananConsumer(AsyncConsumer):
	
	async def websocket_connect(self, event):
		# print(self.scope['url_route']['kwargs']['id'])
		await self.send({
			"type":"websocket.accept",
			# 'text':'hello'
			})
		data = await self.get_data(self.scope['url_route']['kwargs']['id'])
		# await self.get_product(await data.product)
		pesanan = data[0]
		product = data[1]
		client = data[2]
		# dataProduct = await data.product
		my_data = {
			'kwitansi':pesanan.kwitansi,
			'keterangan':pesanan.Keterangan,
			'payment': pesanan.get_statusPembayaran_display(),
			'product':product.namaProduct,
			'total':pesanan.total,
			'nama':client.nama_Client,
			'telp':client.noTelp_Client,
			'alamat':client.alamat_Client,
			'kota':client.kota_Client,
			'approve':data[3],
			'teknisi':data[5],
			'spkProgress':data[4]
		}
		# await asyncio.sleep(3)
		await self.send({
			"type":"websocket.send",
			"text":json.dumps(my_data),
			})

	async def websocket_receive(self, event):
		print("receive", event)

	async def websocket_disconnect(self, event):
		print("disconnect", event)

	@database_sync_to_async
	def get_data(self, id):
		data = PesananModel.objects.get(id=id)
		product = data.product
		client = data.client
		approv = data.ApprovPesanan.approve if hasattr(data, 'ApprovPesanan') else False
		spk = data.SPK if hasattr(data, 'SPK') else '-'
		if spk != '-':
			progress = spk.get_status_display()
			teknisi = spk.teknisi.username
		else: teknisi, progress = '-', '-'

		dataAll = [data, product, client, approv, progress, teknisi.upper()]
		return dataAll
