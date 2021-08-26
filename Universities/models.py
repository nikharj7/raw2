from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class University(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	University_Name = models.CharField(max_length=500, null=True, blank=True)
	File = models.FileField(null=True, blank=True, upload_to='University_list')
	activated = models.BooleanField(default=False)

	def __str__(self):
		return self.University_Name

