from django.shortcuts import render, get_object_or_404, redirect
from crm.models import Client, City, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ClientForm

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
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_details', pk=client.id)
    else:
        form = ClientForm()
    return render(request, 'crm/client_new.htm', {'form': form})
                                                     
                                                     
@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_details', pk=client.id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'crm/client_edit.htm', {'form': form, 'client':client})

def login_view(request):
    next_page = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_page)
        else:
            return render(request, 'crm/login_view.htm', {'login_failed':True})
    else:
        return render(request, 'crm/login_view.htm', {})
