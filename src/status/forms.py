from django import forms
from .models import ProgressBody

class ProgressBodyForm(forms.ModelForm):
    
    class Meta:
        model = ProgressBody
        fields = ['preview_check', 'comment']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['preview_check'].label = 'Request a Website Preview' 
        self.fields['comment'].label = 'Additional Comments'
        
        self.fields['comment'].widget.attrs.update({'class': 'input_classes'})
        self.fields['preview_check'].widget.attrs.update({'class': 'check_classe'})
        
    