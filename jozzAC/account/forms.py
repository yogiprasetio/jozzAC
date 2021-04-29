from django import forms
from .models import Account

class accountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username','jabatan')
