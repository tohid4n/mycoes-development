from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from .forms import OfferForm
from .models import Offer
from user_profile.models import PurchasedOffer


class OfferView(LoginRequiredMixin, generic.CreateView):
    template_name = 'offer.html'
    form_class = OfferForm
    
    def get_success_url(self):
        return reverse('status:home')
    
    def form_valid(self, form):
        offers = Offer.objects.filter(user=self.request.user).order_by('-timestamp')
        latest_offer = offers.first()
    
        if not latest_offer:
            # If no offer has been made by the user, allow them to make a new offer
            form.instance.user = self.request.user
            return super().form_valid(form)
        
        try:
            # Check if there is a PurchasedOffer for the latest_offer
            purchased_offer = PurchasedOffer.objects.get(offer=latest_offer, user=self.request.user)
            # If the offer has been paid, allow the user to make a new offer
            form.instance.user = self.request.user
            return super().form_valid(form)
        except PurchasedOffer.DoesNotExist:
            # If the PurchasedOffer does not exist, prevent the user from making a new offer
            messages.warning(self.request, "Only one offer at a time is allowed.")
            return redirect('orders:make-offer')
        

        
       
        
