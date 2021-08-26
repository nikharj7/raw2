from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile = models.ImageField(upload_to='member_profile_picture', null=True, blank=True, default='default.png')
	first_name = models.CharField(max_length=50, null=True, blank=True)
	middle_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	primary_phone = models.CharField(max_length=10, null=True, blank=True)
	secondry_phone = models.CharField(max_length=10, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=50, null=True, blank=True)
	pin_code = models.CharField(max_length=6,null=True,blank=True,unique=True)
	package = models.CharField(max_length=50, null=True, blank=True)
	amount = models.CharField(max_length=50, null=True, blank=True)
	payment_id = models.CharField(max_length=50, null=True, blank=True)
	address_1 = models.CharField(max_length=500, null=True, blank=True)
	address_2 = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=500, null=True, blank=True)
	Country = models.CharField(max_length=50, null=True, blank=True)
	document = models.FileField(upload_to='Member_documents', null=True, blank=True)
	Paid = models.BooleanField(default=False)
	Terms_and_Conditions = models.BooleanField(default=False)
	def extra(middle_name):
		if middle_name == None:
			return ' '
		if address_2 == None:
			return ' '

	def __str__(self):
		return self.user.username
	


class Add_College_and_University(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	Profile_Picture = models.FileField(null=True, blank=True, upload_to='CollegeProfile', default='default.png')
	College_or_University_Name = models.CharField(max_length=100, null=True, blank=True)
	Course = models.CharField(max_length=100, null=True, blank=True)
	Stream = models.CharField(max_length=100, null=True, blank=True)
	City = models.CharField(max_length=100, null=True, blank=True)
	Pin_Code = models.IntegerField(null=True, blank=True)
	slug = models.CharField(max_length=50, null=True, blank=True)

	# def nice(Course):
	# 	if Course

	def __str__(self):
		return self.College_or_University_Name

        
        
#             