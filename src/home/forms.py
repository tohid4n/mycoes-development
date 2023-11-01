from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'about']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['name'].label = 'Name' 
        self.fields['email'].label = 'Email'
        self.fields['about'].label = 'About'
        
        self.fields['name'].widget.attrs.update({'class': 'contact_classes'})
        self.fields['email'].widget.attrs.update({'class': 'contact_classes'})
        self.fields['about'].widget.attrs.update({'class': 'about_contact_class'})
       
        
        


