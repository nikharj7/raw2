from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member_Email(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title


class Student_Email(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title


class Company_Email(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title

class Student_Activity_Email(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Education = models.CharField(max_length=50, null=True, blank=True)
	Sports = models.CharField(max_length=50, null=True, blank=True)
	Level = models.CharField(max_length=50, null=True, blank=True)
	Medal = models.CharField(max_length=50, null=True, blank=True)
	Number_of_Medals = models.CharField(max_length=50, null=True, blank=True)
	Certificate = models.FileField(upload_to='Student_Certificate')
	Performing_Arts = models.CharField(max_length=50, null=True, blank=True)
	Performing_Arts_if_any = models.CharField(max_length=500, null=True, blank=True)
	def __str__(self):
		return self.user.username