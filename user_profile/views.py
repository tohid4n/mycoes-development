from django.db.models import Sum
from time import sleep
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import OfferForm
from .models import Offer, OfferMilestone
from django.contrib import messages
from django.conf import settings
from .forms import CustomPayPalPaymentsForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt




class OfferView(LoginRequiredMixin, CreateView):
    template_name = 'offer.html'
    form_class = OfferForm
    success_url = reverse_lazy('user_profile:offers-billing')  # Define the URL to redirect to after successful form submission

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

            offers_data = []

            for offer in user_offers:
                # Retrieve milestones specific to the selected offer
                all_offer_milestones = offer.milestones.all()
                offer_milestones = offer.milestones.filter(paid=False).order_by('created_at')
                next_milestone = offer_milestones.first()

                total_ammount = all_offer_milestones.aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
                paid_ammount = offer.milestones.filter(paid=True).aggregate(sum_ammount=Sum('ammount'))['sum_ammount'] or 0
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
                'offers_data': offers_data,
            })

        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        next_milestone_id = request.POST.get('next_milestone_id')
        request.session['next_milestone_id'] = next_milestone_id

        sleep(1)
        return redirect('user_profile:paypal-payment', next_milestone_id=next_milestone_id)
    
    
@method_decorator(csrf_exempt, name='dispatch')
class PaypalPaymentView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        # Retrieve milestone data from sessions
        next_milestone_id = self.request.session.get('next_milestone_id')

        try:
            # Check if next_milestone_id is present
            if not next_milestone_id:
                raise Http404
            # Retrieve the milestone using next_milestone_id
            milestone = OfferMilestone.objects.get(id=next_milestone_id)
        except OfferMilestone.DoesNotExist:
            # Handle the case where the milestone is not found
            raise Http404
        
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': milestone.ammount, 
            'item_name': milestone.offer.title,  
            'invoice': str(milestone.id), 
            'item_number': str(milestone.milestone_number),
            'currency_code': 'USD', 
            'notify_url': f'http://{request.get_host()}{reverse("paypal-ipn")}',
            'return_url': f'http://{request.get_host()}{reverse("user_profile:paypal-payment-success", kwargs={"next_milestone_id": next_milestone_id})}',
            'cancel_return': f'http://{request.get_host()}{reverse("user_profile:paypal-payment", kwargs={"next_milestone_id": next_milestone_id})}?message=cancel',

        }

        form = CustomPayPalPaymentsForm(initial=paypal_dict)
        
        context = {
            'form': form,
            'milestone': milestone  
        }
        
        message = request.GET.get('message', None)

        if message == 'notify':
            messages.info(request, 'Something happened on the Paypal side, Please retry.')
        elif message == 'cancel':
            messages.warning(request, 'Payment was canceled.')

        return render(request, 'paypal-payment.html', context)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            # Redirect to your custom 404 page
            return render(request, '404.html', status=404)
    
    
    

class PaypalPaymentSuccessView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'paypal-payment-success.html' 
    


class ProfileTranscationsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile-transcations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve paid transactions
        transactions = OfferMilestone.objects.filter(offer__user=self.request.user, paid=True)

        context['transactions'] = transactions
        return context  
    


class CustomLogoutView(LoginRequiredMixin, LogoutView):
  def get_success_url(self):
    success_url = super(CustomLogoutView, self).get_success_url()
    messages.add_message(
      self.request, messages.SUCCESS,
      'You have successfully logged out.'
    )
    return reverse('home:home-page')   