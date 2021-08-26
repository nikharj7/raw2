from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Profile = models.FileField( null=True, blank=True, upload_to='Student_Profile_Picture', default='default.png')
	First_Name = models.CharField(max_length=50,  null=True, blank=True)
	Middle_Name = models.CharField(max_length=50, null=True, blank=True)
	Last_Name = models.CharField(max_length=20,  null=True, blank=True)
	Mobile = models.CharField(max_length=14,  null=True, blank=True)
	Email = models.EmailField()
	DOB = models.DateField(null=True, blank=True)
	Gender = models.CharField(max_length=10,null=True, blank=True)
	Facebook_Profile = models.CharField(max_length=50, null=True, blank=True)
	Linkedin = models.CharField(max_length=50, null=True, blank=True)
	Twitter_Profile = models.CharField(max_length=50, null=True, blank=True)
	Address_1 = models.CharField(max_length=200, null=True, blank=True)
	Address_2 = models.CharField(max_length=200, null=True, blank=True)
	City = models.CharField(max_length=20, null=True, blank=True)
	State = models.CharField(max_length=20, null=True, blank=True)
	Pin_Code = models.IntegerField(null=True, blank=True)
	Country = models.CharField(max_length=20, null=True, blank=True)
	Course = models.CharField(max_length=50, null=True, blank=True)
	University_Name = models.CharField(max_length=20, null=True, blank=True)
	Year_Start = models.DateField(null=True, blank=True)
	Year_End = models.DateField(null=True, blank=True)
	Terms_and_Conditions = models.BooleanField(default=False)
	University_address = models.CharField(max_length=20, null=True, blank=True)
	University_address2 = models.CharField(max_length=20, null=True, blank=True)
	University_City = models.CharField(max_length=20, null=True, blank=True)
	University_State = models.CharField(max_length=20, null=True, blank=True)
	University_Pin_Code = models.CharField(max_length=20, null=True, blank=True)
	University_Country = models.CharField(max_length=20, null=True, blank=True, default="India")


	def __str__(self):
		return self.First_Name + ' ' + self.Last_Name


class New_Student(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	File = models.FileField(upload_to='New_Student_csv')
	name = models.CharField(max_length=500, null=True, blank=True)
	activated = models.BooleanField(default=False)
	def __str__(self):
		return self.name