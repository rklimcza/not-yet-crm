from django.db import models
from django.utils import timezone
from datetime import date


class Client(models.Model):
	
	first_name = models.CharField(max_length = 20)
	second_name = models.CharField(max_length = 20)
	city = models.ManyToManyField("City")
	email = models.EmailField()
	phone_number = models.CharField(max_length = 20)
	comment = models.TextField()
	contacts = models.ManyToManyField("Contact")


class City(models.Model):
	
	name = models.CharField(max_length = 20)
	
	
class Contact(models.Model):
	
	contact_ways = (
    ('phone', 'telefon'),
    ('email', 'e-mail'),
	('meeting', 'spotkanie'),
    ('class', 'szkolenie'),
	)
	
	date = models.DateField(default=date.today)
	way = models.CharField(max_length=10, choices=contact_ways)
	comment = models.TextField()
	
