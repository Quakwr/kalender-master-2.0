from django import forms
from .models import Gasto

class NuevoGasto(forms.ModelForm):
	class Meta:
		model = Gasto
		exclude = ["fecha"]