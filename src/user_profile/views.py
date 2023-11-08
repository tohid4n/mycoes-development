from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PurchasedOffer
from orders.models import Offer

from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect

class OrderView(LoginRequiredMixin, generic.TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offers = Offer.objects.filter(user=self.request.user)
        purchased_offers = PurchasedOffer.objects.filter(user=self.request.user)
        context['offers'] = offers
        context['purchased_offers'] = purchased_offers
        return context
    
    def get_template_names(self):
        # Override get_template_names to return different templates based on conditions
        purchased_offers = self.get_context_data().get('purchased_offers')
        if purchased_offers.exists():
            return ['orders.html']
        else:
            return ['no-order.html']



class TransactionsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'transactions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offers = Offer.objects.filter(user=self.request.user)
        purchased_offers = PurchasedOffer.objects.filter(user=self.request.user)
        context['offers'] = offers
        context['purchased_offers'] = purchased_offers
        return context

    def get_template_names(self):
        # Override get_template_names to return different templates based on conditions
        purchased_offers = self.get_context_data().get('purchased_offers')
        if purchased_offers.exists():
            return ['transactions.html']
        else:
            return ['no-transactions.html']



class CustomLogoutView(LogoutView):
  def get_success_url(self):
    success_url = super(CustomLogoutView, self).get_success_url()
    messages.add_message(
      self.request, messages.SUCCESS,
      'You have successfully logged out.'
    )
    return reverse('home:home-page')   