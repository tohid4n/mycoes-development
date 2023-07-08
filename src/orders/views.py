from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from .forms import OfferForm


class OfferView(LoginRequiredMixin, generic.CreateView):
    template_name = 'offer.html'
    form_class = OfferForm
    
    def get_success_url(self):
        return reverse('status:home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
