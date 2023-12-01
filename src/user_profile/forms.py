from django import forms
from .models import Offer
from payments import get_payment_model


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['title', 'description', 'timeline', 'budget', 'attached_files']

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = "Project Title"
        self.fields['description'].label = "How can we help you?"
        self.fields['timeline'].label = "What's your timeline?"
        self.fields['budget'].label = "What's your budget range?"
        self.fields['attached_files'].label = 'Attach Files(Optional)'
        
        
        # Add classes to the fields
        self.fields['title'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['description'].widget.attrs.update({'class': 'offer_form_area_input_classes', 'rows': '4'})
        self.fields['attached_files'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['timeline'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['budget'].widget.attrs.update({'class': 'offer_form_input_classes'})



        
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = get_payment_model()
        fields = ["variant", "currency", "total"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the fields as not required
        self.fields["variant"].required = False
        self.fields["currency"].required = False
        self.fields["total"].required = False
        