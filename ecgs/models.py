from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ECG(models.Model):
	paciente = models.ForeignKey(User, related_name="paciente", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	archivo = models.FileField(upload_to='historial/%Y/%m/%d/')