from django.db import models


class Courses(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Streams(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name



class State(models.Model):
	State = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.State

class Pin_Code(models.Model):
	State = models.ForeignKey(State, on_delete=models.CASCADE)
	Pin_Code = models.CharField(max_length=6, null=True, blank=True)

	def __str__(self):
		return self.Pin_Code 


class Education(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

class Sport(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

class Performing_Art(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

