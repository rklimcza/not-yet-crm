from django.contrib import admin
from .models import Client, City, Contact, Task

admin.site.register(Client)
admin.site.register(City)
admin.site.register(Contact)
admin.site.register(Task)
