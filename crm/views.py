from django.shortcuts import render, get_object_or_404
from crm.models import Client, City, Contact


def client_list(request, pk=0):
	
	pk = int(pk)
	if pk == 0:
		clients = Client.objects.all().order_by('city', 'first_name')
	else:
		clients = Client.objects.filter(city=pk).order_by('city', 'first_name')
		
	cities = City.objects.all().order_by('id')
	
	return render(request, 'crm/client_list.htm', {'clients': clients,
												   'cities':cities,
												   'city_now':pk,
												  })


def client_details(request, pk):
	pk = int(pk)
	client = get_object_or_404(Client, id=pk)
	contacts = Contact.objects.filter(clients=pk).order_by('date')
	
	return render(request, 'crm/client_details.htm', {'client': client,
												      'contacts': contacts,
													 })
