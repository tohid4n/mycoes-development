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
from .forms import OfferForm, PaymentForm

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from decimal import Decimal
from payments import get_payment_model
from .models import Offer, OfferMilestone, CommunicationPlatforms


from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

from decimal import Decimal
from payments import get_payment_model





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
    
    

  
class CreatePaymentView(LoginRequiredMixin, View):
    
    def get(self, request):
        form = PaymentForm()
        return render(request, "create_payment.html", {"form": form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            next_milestone_id = request.POST.get('next_milestone_id')
            form.instance.variant = "stripe"
            form.instance.currency = "USD"
            form.instance.total = Decimal(request.POST.get('ammount', 0))
            form.instance.description = request.POST.get('title')

            payment = form.save(commit=False)
            payment.save()

            return redirect(reverse('user_profile:payment-details', args=[payment.id]))

        


class PaymentDetailsView(View):
    def get(self, request, payment_id):
        payment = get_object_or_404(get_payment_model(), id=payment_id)
        try:
            form = payment.get_form(data=request.POST or None)
        except RedirectNeeded as redirect_to:
            return redirect(str(redirect_to))
        return render(request, "payment.html", {"form": form, "payment": payment})


class PaymentSuccessView(View):
    def get(self, request):
        return HttpResponse("Payment succeeded.")


class PaymentFailureView(View):
    def get(self, request):
        return HttpResponse("Payment failed.")
    

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