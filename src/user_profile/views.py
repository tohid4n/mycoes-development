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
from .models import Offer, OfferMilestone, CommunicationPlatforms




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

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_offers = Offer.objects.filter(user=self.request.user)
            communication_platforms = CommunicationPlatforms.objects.first()

            offers_data = []

            for offer in user_offers:
                # Retrieve milestones specific to the selected offer
                all_offer_milestones = offer.milestones.all()
                offer_milestones = offer.milestones.filter(paid=False)
                next_milestone = offer_milestones.first()

                total_ammount = all_offer_milestones.aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
                paid_ammount = offer_milestones.filter(paid=True).aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
                remaining_ammount = total_ammount - paid_ammount

                offers_data.append({
                    'offer': offer,
                    'all_offer_milestones': all_offer_milestones,
                    'next_milestone': next_milestone,
                    'total_ammount': total_ammount,
                    'remaining_ammount': remaining_ammount,
                })

            # Update the context with the new data
            context.update({
                'user_offers': user_offers,
                'communication_platforms': communication_platforms,
                'offers_data': offers_data,
            })

        return self.render_to_response(context)

    def post(self, request):
        offer_id = request.POST.get('selected_offer_id')
        selected_offer = get_object_or_404(Offer, id=offer_id, user=request.user)
        offer_milestones = selected_offer.milestones.filter(paid=False)

        if offer_milestones.exists():
            next_milestone = offer_milestones.first()

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

        return super().post(request)




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