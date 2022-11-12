from django import forms
from .models import Gasto, calendario

class NuevoGasto(forms.ModelForm):
	class Meta:
		model = Gasto
		exclude = ["fecha"]

		
class lista(forms.ModelForm):
	titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Cuenta a pagar'}), label=False)
	fecha = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Fecha de pago.'}), label=False)
	class Meta:
		model = calendario
		fields = ['titulo', 'fecha']

class actualizarform(forms.ModelForm):
	titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = calendario
		fields = ['titulo', 'fecha', 'hecho']