from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from ecgs.forms import *
from ecgs.models import *
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

#Ver perfil al iniciar sesión
class ViewProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		user = User.objects.get(pk=request.user.pk)

		try:
			profile = Profile.objects.get(user=user)
			print(request.user.user.doctor)

		except:
			profile = None
	
		context = {
			'profile': profile,
		}
		return render(request,template_name, context)

class ListViewPacientes(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listPacientes.html"
		doctor = User.objects.get(pk=request.user.pk)
		perfiles= Profile.objects.filter(doctor=doctor)

		context = {
			'perfiles': perfiles
		}
		return render(request, template_name, context)

class DetailViewPaciente(View):
	@method_decorator(login_required)
	def get(self,request, username):
		template_name = "accounts/detailPaciente.html"
		paciente = get_object_or_404(User, username=username)
		perfil = Profile.objects.get(user=paciente)
		NuevoECGForm = ECGCreateForm()
		ecgs = ECG.objects.filter(paciente=paciente)
		print(ecgs)
		context = {
			'paciente': paciente,
			'perfil': perfil,
			'NuevoECGForm': NuevoECGForm,
			'ecgs': ecgs,
		}
		return render(request, template_name, context)
	def post(self,request, username):
		paciente = get_object_or_404(User, username=username)
		perfil = Profile.objects.get(user=paciente)

		NuevoECGForm = ECGCreateForm(files=request.FILES)
		if NuevoECGForm.is_valid():
			NuevoECG = NuevoECGForm.save(commit=False)
			NuevoECG.paciente = paciente
			NuevoECG.save()

		return redirect("accounts:DetailViewPaciente", paciente.username)

class CreateViewPaciente(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createPaciente.html"
		NuevoUserPacienteForm = UserPacienteCreateForm()
		NuevoProfilePacienteForm = ProfilePacienteCreateForm() 

		context = {
			'NuevoUserPacienteForm': NuevoUserPacienteForm,
			'NuevoProfilePacienteForm': NuevoProfilePacienteForm
		}
		return render(request, template_name, context)
	def post(self, request):
		NuevoUserPacienteForm = UserPacienteCreateForm(data=request.POST, files=request.FILES)
		NuevoProfilePacienteForm = ProfilePacienteCreateForm(data=request.POST, files=request.FILES)

		users = User.objects.all().count() + 1
		doctor = User.objects.get(pk=request.user.pk)
		
		if NuevoUserPacienteForm.is_valid():
			NuevoUserPaciente = NuevoUserPacienteForm.save(commit=False)
			NuevoUserPaciente.username = str("PX") + str(users)
			NuevoUserPaciente.set_password('concurso')
			NuevoUserPaciente.save()

		if NuevoProfilePacienteForm.is_valid():
			NuevoProfilePaciente = NuevoProfilePacienteForm.save(commit=False)
			NuevoProfilePaciente.user = NuevoUserPaciente
			NuevoProfilePaciente.doctor = doctor
			NuevoProfilePaciente.save()			
	
		return redirect("accounts:ListViewPacientes")

class DeleteViewPaciente(DeleteView):
	model = User
	success_url = reverse_lazy('accounts:ListViewPacientes')