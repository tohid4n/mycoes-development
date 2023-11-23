from django.db.models import Sum
from time import sleep
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from requests import request
from stripe import PaymentIntent

from user_profile.models import CommunicationPlatforms, Offer
from .forms import OfferForm

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from decimal import Decimal
from payments import get_payment_model
from .models import Offer, offer_milestone, CommunicationPlatforms




class OfferView(LoginRequiredMixin, CreateView):
    template_name = 'offer.html'
    form_class = OfferForm
    success_url = reverse_lazy('user_profile:profile-offers-billing')  # Define the URL to redirect to after successful form submission

    def form_valid(self, form):
        # Set the user field to the authenticated user and save the form
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Your offer has been submitted successfully. To proceed, click on your preferred communication platforms for the next steps.")
        sleep(2.5)
        return super().form_valid(form)
    
    



Payment = get_payment_model()

class BillingView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'billing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_offers = Offer.objects.filter(user=self.request.user)
            communication_platforms = CommunicationPlatforms.objects.first()
            all_milestones = offer_milestone.objects.filter(offer__user=self.request.user)
            non_paid_milestones = offer_milestone.objects.filter(offer__user=self.request.user, paid=False)
            next_milestone = non_paid_milestones.first()
            total_ammount = all_milestones.aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
            paid_ammount = all_milestones.filter(paid=True).aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
            remaining_ammount = total_ammount - paid_ammount

            context.update({
                'user_offers': user_offers,
                'communication_platforms': communication_platforms,
                'all_milestones': all_milestones,
                'next_milestone':next_milestone,
                'total_ammount': total_ammount,
                'paid_ammount': paid_ammount,
                'remaining_ammount': remaining_ammount,
            })

        return context


    def post(self, request):
        non_paid_milestones = offer_milestone.objects.filter(offer__user=self.request.user, paid=False)
        
        if non_paid_milestones.exists():
            next_milestone = non_paid_milestones.first()

            # Create a payment for the next milestone using the determined variant
            payment = Payment.objects.create(
                variant='default',
                description=f'Payment for milestone: {next_milestone}',
                total=next_milestone.ammount,
                currency='USD',
                billing_name='MyCoes',
                billing_address_1='Khedekar layout Near Central Bus Stand',
                billing_city='Gulbarga',
                billing_postcode='585103',
                billing_country_code='IN',
                billing_country_area='India',
                customer_ip_address=request.META.get('HTTP_X_REAL_IP', request.META.get('REMOTE_ADDR', ''))
            )

            if payment.is_successful():
                next_milestone.paid = True
                next_milestone.payment_status = 'confirmed'
                messages.success(request, 'Payment successful.')
            else:
                next_milestone.payment_status = 'error'
                messages.error(request, 'Payment failed.')

            next_milestone.save()




class ProfileTranscationsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile-transcations.html' 
    

          
    

    
    







    

    


class CustomLogoutView(LoginRequiredMixin, LogoutView):
  def get_success_url(self):
    success_url = super(CustomLogoutView, self).get_success_url()
    messages.add_message(
      self.request, messages.SUCCESS,
      'You have successfully logged out.'
    )
    return reverse('home:home-page')   