from django.db import models
from django.utils import timezone

class Client(models.Model):
	first_name = models.CharField(max_length = 20)
	second_name = models.CharField(max_length = 20)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 20)
	
