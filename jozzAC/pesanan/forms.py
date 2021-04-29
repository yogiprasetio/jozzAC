from django import forms
from .models import PesananModel

class PesananForm(forms.ModelForm):
    class Meta:
        model = PesananModel
        fields = ('product','client', 'Keterangan', 'jumlah_Ac', 'total')

        widgets={
        	'Keterangan': forms.Textarea(attrs={
        		'name':"keterangan",
        		'id':"inputKeterangan",
        		'class':"form-control",
        		'style': 'height: 50px',
                'aria-describedby':"emailHelp",
        		}),
        	'total':forms.NumberInput(attrs={
        		'name':"total",
        		'class':"form-control",
        		'id':"inputTotal",
                'aria-describedby':"emailHelp",
        		})
        }