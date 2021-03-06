from django import forms
from .models import Client, Contact

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'city', 'email', 
                  'phone_number', 'comment',
                 )
                 
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('way', 'date', 'comment')
