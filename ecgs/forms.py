from django import forms
from .models import *

class ECGCreateForm(forms.ModelForm):
	class Meta:
		model = ECG
		fields = ('archivo',)
