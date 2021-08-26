from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Profile = models.FileField(upload_to='Company_profile', null=True, blank=True, default='default.png')
	Company_Name = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	Mobile = models.CharField(max_length=10, null=True, blank=True)
	Industry = models.CharField(max_length=50, null=True, blank=True)
	Orgnization = models.CharField(max_length=50, null=True, blank=True)
	Address_1 = models.CharField(max_length=500, null=True, blank=True)
	Address_2 = models.CharField(max_length=500, null=True, blank=True)
	City = models.CharField(max_length=500, null=True, blank=True)
	State = models.CharField(max_length=500, null=True, blank=True)
	Pin_Code = models.IntegerField(null=True, blank=True)
	Country = models.CharField(max_length=500, null=True, blank=True)
	Terms_and_Conditions = models.BooleanField(default=False)



	def __str__(self):
		return self.Company_Name

class Internships(models.Model):
	Title = models.CharField(max_length=50)
	Description = models.TextField()
	Course = models.CharField(max_length=50)
	Qualification = models.CharField(max_length=50)
	Number_of_Openings = models.IntegerField()
	Experience = models.IntegerField()
	Salary = models.IntegerField()
	Application_Process = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.Title

class Jobs(models.Model):
	Title = models.CharField(max_length=50)
	Description = models.TextField()
	Course = models.CharField(max_length=50)
	Qualification = models.CharField(max_length=50)
	Number_of_Openings = models.IntegerField()
	Experience = models.IntegerField()
	Salary = models.IntegerField()
	Application_Process = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.Title



class Industry(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

class Orgnization(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name