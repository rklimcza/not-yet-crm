from django.db import models
from django.utils import timezone
from datetime import date


class Client(models.Model):
	
	first_name = models.CharField(max_length=20, verbose_name='Imię')
	last_name = models.CharField(max_length=20, verbose_name='Nazwisko')
	city = models.ForeignKey('City', verbose_name='Miasto')
	email = models.EmailField(verbose_name='E-mail')
	phone_number = models.CharField(max_length=20, verbose_name='Nr telefonu')
	comment = models.TextField(verbose_name='Komentarz', blank=True)
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name


class City(models.Model):
	
	name = models.CharField(max_length=20, verbose_name='Nazwa')
	
	def __str__(self):
		return ' ' + self.name
	
	
class Contact(models.Model):
	
	contact_ways = (
    ('phone', 'telefon'),
    ('email', 'e-mail'),
	('meeting', 'spotkanie'),
    ('class', 'szkolenie'),
	)
	
	date = models.DateField(default=date.today(), verbose_name='Data')
	way = models.CharField(max_length=10, choices=contact_ways,
		  verbose_name='Sposób')
	clients = models.ManyToManyField('Client', verbose_name='Klienci')
	comment = models.TextField(verbose_name='Komentarz')
	
	def __str__(self):
		return str(self.id) + '. ' + str(self.date) + ' ' + self.way
