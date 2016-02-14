from django.db import models
from django.utils import timezone
from datetime import date

class Client(models.Model):
	first_name = models.CharField(max_length = 20)
	second_name = models.CharField(max_length = 20)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 20)
	comment = models.TextField()

class City(models.Model):
	name = models.CharField(max_length = 20)
	
class Contact(models.Model):
	date = models.DateField(default=date.today)
	
