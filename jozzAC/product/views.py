from django.shortcuts import render
from .models import ProductModel
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin

# Create your views here.
class produkView(ListView):
	model = ProductModel
	template_name = 'product/productView.html'
	context_object_name = 'objects'

class productDetail(ModelFormMixin, DetailView):
	# model = 
	pass