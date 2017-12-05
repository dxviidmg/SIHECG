from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, related_name="user", null=True, blank=True)
	phone = models.CharField(max_length=12, verbose_name="Teléfono")
	age = models.IntegerField(verbose_name="Edad")
	doctor = models.ForeignKey(User, related_name="doctor", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.user)

def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)	