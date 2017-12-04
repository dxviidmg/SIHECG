from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^accounts/create/paciente/$', views.CreateViewPaciente.as_view(), name="CreateViewPaciente"),
	url(r'^accounts/list/pacientes/$', views.ListViewPacientes.as_view(), name="ListViewPacientes"),
	url(r'^accounts/detail/(?P<username>[-\w]+)/$', views.DetailViewPaciente.as_view(), name="DetailViewPaciente"),
	url(r'^accounts/profile/$', views.ViewProfile.as_view(), name="ViewProfile"),
    ]