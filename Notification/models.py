from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Member.models import *
# Create your models here.

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	title = models.CharField(max_length=500)
	message = models.TextField()
	viewd = models.BooleanField(default=False)
	

# @receiver(post_save, sender=User)
# def create_message(sender, **kwargs):
# 	if kwargs.get('created', False):
# 		Notification.objects.create(user=kwargs.get('instance'), title="welcome", message="thanks")


class Member_Notification(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title


class Student_Notification(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title


class Company_Notification(models.Model):
	Title = models.CharField(max_length=500, null=True, blank=True)
	Description = models.TextField()

	def __str__(self):
		return self.Title




