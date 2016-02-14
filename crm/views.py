from django.shortcuts import render
from crm.models import Client, City, Contact


def client_list(request):
	clients = Client.objects.all().order_by('city', 'first_name')
	cities = City.objects.all().order_by('id')
	
	return render(request, 'crm/client_list.htm', {'clients': clients,
												   'cities':cities, 
												  })
