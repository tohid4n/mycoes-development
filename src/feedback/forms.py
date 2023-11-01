from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text_feedback',]
        
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_feedback'].label = '' 
        
        self.fields['text_feedback'].widget.attrs.update({'class': 'text_feedback'})
    