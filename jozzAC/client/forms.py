from django import forms
from .models import ClientModel

class clientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ('nama_Client','noTelp_Client', 'email_Client', 'alamat_Client', 
        			'kecamatan_Client', 'kelurahan_Client', 'kodePos_Client', 'kota_Client')

        widgets={
        	'nama_Client': forms.TextInput(attrs={
        		'name':"nama",
        		'id':"inputName", 
        		'aria-describedby':"emailHelp",
        		'class':'form-control'
        		}),
        	'noTelp_Client': forms.TextInput(attrs={
        		'name':"phone",
        		'class':"form-control",
        		'id':"inputPhone",
                'aria-describedby':"emailHelp",
        		}),
        	'email_Client': forms.EmailInput(attrs={
        		'name':"email",
        		'class':"form-control",
        		'id':"inputEmail",
                'aria-describedby':"emailHelp",
        		}),
        	'alamat_Client': forms.Textarea(attrs={
        		'name':"alamat",
        		'id':"inputAddress",
        		'class':"form-control",
        		'style': 'height: 50px',
                'aria-describedby':"emailHelp",
        		})
        }