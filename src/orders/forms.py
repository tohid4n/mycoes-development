from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
    
        fields = ['title', 'description', 'development_category', 'date', 'budget', 'attached_files']
        
        
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'budget': forms.widgets.NumberInput(attrs={'placeholder': '$'})
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['title'].label = 'Project Name' 
        self.fields['description'].label = 'Website Requirements'
        self.fields['development_category'].label = 'Select Development Category'
        self.fields['date'].label = 'What is your desired deadline for completion of the project?'
        self.fields['budget'].label = 'Estimated Budget?'
        self.fields['attached_files'].label = 'Attach Files'

        
        self.fields['title'].widget.attrs.update({'class': 'input_classes'})
        self.fields['description'].widget.attrs.update({'class': 'input_classes'})
        self.fields['development_category'].widget.attrs.update({'class': 'input_classes'})
        self.fields['attached_files'].widget.attrs.update({'class': 'input_classes'})
        self.fields['date'].widget.attrs.update({'class': 'input_classes'})
        self.fields['budget'].widget.attrs.update({'class': 'input_classes'})
    
        
        
        
