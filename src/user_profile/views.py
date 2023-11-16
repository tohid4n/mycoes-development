from time import sleep
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import OfferForm



class PricingView(generic.TemplateView):
    template_name = 'profile.html' 



class CustomLogoutView(LogoutView):
  def get_success_url(self):
    success_url = super(CustomLogoutView, self).get_success_url()
    messages.add_message(
      self.request, messages.SUCCESS,
      'You have successfully logged out.'
    )
    return reverse('home:home-page')   




class OfferView(LoginRequiredMixin, CreateView):
    template_name = 'offer.html'
    form_class = OfferForm
    success_url = reverse_lazy('user_profile:profile')

    def form_valid(self, form):
        # Set the user field to the authenticated user
        form.instance.user = self.request.user

        # Extract selected services from the form and set them on the model instance
        selected_services = self.request.POST.getlist('selected_services')
        form.instance.selected_services = ', '.join(selected_services)
        
        # Save the form
        form.save()

        messages.success(self.request, "Your offer has been submitted successfully. To proceed, click on your preferred communication platforms for the next steps.")
        sleep(2.5)
        return super().form_valid(form)
