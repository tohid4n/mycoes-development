from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_classes = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded focus:ring-black focus:border-black  block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-black dark:focus:border-black'
        
        self.fields['full_name'].widget.attrs.update({'class': input_classes})
        self.fields['email'].widget.attrs.update({'class': input_classes})
        self.fields['topic'].widget.attrs.update({'class': input_classes})
        self.fields['message'].widget.attrs.update({'class': input_classes})