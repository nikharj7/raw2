from django.db import models

# Create your models here.
class Member_Wait_list(models.Model):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	primary_phone = models.CharField(max_length=10, null=True, blank=True)
	pin_code = models.CharField(max_length=6,null=True,blank=True)
	
	

	def __str__(self):
		return self.first_name