from django.shortcuts import render, get_object_or_404, redirect
from crm.models import Client, City, Contact, Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ClientForm, ContactForm
from datetime import date, timedelta
import datetime


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
                                                   'current':1,
												  })

@login_required
def client_details(request, pk):
	pk = int(pk)
	client = get_object_or_404(Client, id=pk)
	contacts = Contact.objects.filter(clients=pk).order_by('date')
	
	return render(request, 'crm/client_details.htm', {'client': client,
												      'contacts': contacts,
                                                      'current':1,
													 })
                                                     
@login_required
def client_delete(request, pk):
    pk = int(pk)
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect('/')
                                                     
@login_required
def client_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_details', pk=client.id)
    else:
        form = ClientForm()
    return render(request, 'crm/client_new.htm', {'form': form,
                                                  'current':1,
                                                  })
                                                     
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
    return render(request, 'crm/client_edit.htm', {'form': form,
                                                   'client':client,
                                                   'current':1,
                                                   })

@login_required
def contact_new(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            contact.clients.add(pk)
            return redirect('client_details', pk=pk)
    else:
        form = ContactForm()
    return render(request, 'crm/contact_new.htm', {'form': form,
                                                   'client':client,
                                                   'current':1,
                                                   })



@login_required
def task_list(request, range=0):
    end = date.today()
    if range == 'day':
        pass
    elif range == 'week':
        end += datetime.timedelta(weeks=1)
    elif range == 'month':
        end += datetime.timedelta(days=31)
    elif range == 'year':
        end += datetime.timedelta(days=365)
    tasks = Task.objects.filter(date__range=(date.today(), end), done=False).order_by('date')
    return render(request, 'crm/task_list.htm', {'current':2,
                                                 'tasks':tasks,
                                                 'active_range':range,})
