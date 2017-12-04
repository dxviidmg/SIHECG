from django import forms
from .models import *

class UserPacienteCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfilePacienteCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('age', 'phone',)

