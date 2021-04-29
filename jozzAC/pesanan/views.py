from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import PesananModel, approvalModel, pembayaranModel
from account.models import Account
from django.core import serializers

from .forms import PesananForm
from client.forms import clientForm
from account.forms import accountForm

# Create your views here.
class pesananKhusus(CreateView):
	
	model = PesananModel
	form_class = PesananForm
	template_name = 'admin/add.html'
	success_url = 'admin/add.html'

	def get_context_data(self, **kwargs):
	    kwargs['form'] = self.get_form()
	    kwargs['formClient'] = clientForm
	    kwargs['formAccount'] = accountForm
	    kwargs['account'] = Account.objects.filter(jabatan='TEKNISI')
	    return super().get_context_data(**kwargs)

	def post(self, *args, **kwargs):
		print(self.request.POST)
		print(self.request.POST['nama_Client'])
		return super().get(self.request, **kwargs)


class Tracking(ListView):
	
	model = PesananModel
	context_object_name = 'pesanan'
	template_name = 'admin/tracking.html'
	data = serializers.serialize('json', list(model.objects.all()))
	dataApprov = serializers.serialize('json', list(approvalModel.objects.all()))
	dataPayment = serializers.serialize('json', list(pembayaranModel.objects.all()))
	extra_context = {
			'my_list':data,
			'my_payment':dataPayment,
			'my_approv':dataApprov,
			}
