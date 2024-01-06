from django import forms
from .models import ContactModel, E_OfferModel


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
       
        
        

class E_OfferForm(forms.ModelForm):
    class Meta:
        model = E_OfferModel
        fields = ['name', 'email', 'accept', 'about']
        
    def clean(self):
        cleaned_data = super().clean()
        accept = cleaned_data.get('accept')

        if not accept:
            self.add_error('accept', 'You must accept the terms to submit the form.')

        return cleaned_data    
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['name'].label = 'Name' 
        self.fields['email'].label = 'Email'
        self.fields['about'].label = 'Which Services are You going with?'
        self.fields['accept'].label = 'I accept the terms'
        
        self.fields['name'].widget.attrs.update({'class': 'contact_classes'})
        self.fields['email'].widget.attrs.update({'class': 'contact_classes'})
        self.fields['about'].widget.attrs.update({'class': 'about_contact_class'})
        self.fields['accept'].widget.attrs.update({'class': 'accept_contact_class'})
       
        
        


