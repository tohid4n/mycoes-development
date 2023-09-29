from django import forms



class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input_classes'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input_classes'}))
    topic = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input_classes'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input_classes'}))



