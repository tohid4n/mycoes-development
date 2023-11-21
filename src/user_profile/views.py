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
    success_url = reverse_lazy('user_profile:profile-offers')  # Define the URL to redirect to after successful form submission

    def form_valid(self, form):
        # Set the user field to the authenticated user and save the form
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Your offer has been submitted successfully. To proceed, click on your preferred communication platforms for the next steps.")
        sleep(2.5)
        return super().form_valid(form)
    
    



Payment = get_payment_model()

class BillingView(View):
    template_name = 'billing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Make sure the user is authenticated
        if self.request.user.is_authenticated:
            # Get all offers made by the current user
            user_offers = Offer.objects.filter(user=self.request.user)

            # Get communication platforms (assuming there is only one set of platforms for all users)
            communication_platforms = CommunicationPlatforms.objects.first()

            context['user_offers'] = user_offers
            context['communication_platforms'] = communication_platforms

        return context

    def get(self, request):
        # You can modify this logic based on your requirements
        milestones = offer.offer_milestone_set.all()
        if milestones.exists():
            offer_id = milestones.first().offer.id
            offer = get_object_or_404(Offer, pk=offer_id)

            total_amount = offer.total_amount()
            paid_amount = sum(milestone.amount for milestone in milestones.filter(paid=True))
            remaining_amount = total_amount - paid_amount

            context = self.get_context_data()
            context.update({
                'offer': offer,
                'milestones': milestones,
                'total_amount': total_amount,
                'paid_amount': paid_amount,
                'remaining_amount': remaining_amount,
            })

            return render(request, self.template_name, context)

        # Handle the case when there are no milestones available
        return render(request, self.template_name, {'message': 'No milestones available for billing.'})



    def post(self, request, offer_id):
        offer = get_object_or_404(Offer, pk=offer_id)
        milestones = offer.offer_milestone_set.filter(paid=False)

        if milestones.exists():
            next_milestone = milestones.first()

            # Create a payment for the next milestone using the determined variant
            payment = Payment.objects.create(
                variant='default',
                description=f'Payment for milestone: {next_milestone}',
                total=next_milestone.amount,
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
                next_milestone.payment_status = 'confirmed'  # Update based on your payment result
            else:
                next_milestone.payment_status = 'error'

            next_milestone.save()


        return redirect('billing', offer_id)
    




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