from django.shortcuts import render, get_object_or_404, redirect
from crm.models import Client, City, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def client_details(request, pk):
	pk = int(pk)
	client = get_object_or_404(Client, id=pk)
	contacts = Contact.objects.filter(clients=pk).order_by('date')
	
	return render(request, 'crm/client_details.htm', {'client': client,
												      'contacts': contacts,
													 })
                                                     
@login_required
def client_edit(request, pk):
	pk = int(pk)
	client = get_object_or_404(Client, id=pk)
	contacts = Contact.objects.filter(clients=pk).order_by('date')
	
	return render(request, 'crm/client_edit.htm', {'client': client,
												      'contacts': contacts,
													 })

def login_view(request):
    next_page = request.GET.get('next', '/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    fail = False
    if username is not None:
        fail = True
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        return render(request, 'crm/login_view.htm', {'login_failed':fail})
