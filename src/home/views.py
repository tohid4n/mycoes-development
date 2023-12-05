from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import  View, generic
from home.models import E_OfferModel
from .forms import ContactForm, E_OfferForm


class HomePageView(generic.TemplateView):
    template_name = 'home-page.html'
      

class AboutView(generic.TemplateView):
    template_name = 'about.html'
    
    
class ServicesView(generic.TemplateView):
    template_name = 'services.html'    
    
class PricingView(generic.TemplateView):
    template_name = 'pricing.html'        
    
  
class PrivacyPolicyView(generic.TemplateView):
    template_name = 'privacy-policy.html'   
    
class TermsOfServicesView(generic.TemplateView):
    template_name = 'terms-of-services.html'            
   




class E_OfferView(generic.FormView):
    form_class = E_OfferForm
    template_name = 'e-offers.html'

    def get_success_url(self):
        return reverse_lazy("home:e-offer")  # Use reverse_lazy for success_url

    def form_valid(self, form):
        # Check if the registration limit has been reached
        if E_OfferModel.objects.count() >= 5:
            messages.error(
                self.request, "The registration limit has been reached. We appreciate your interest. Contact us for more information."
            )
            return self.form_invalid(form)  # Use form_invalid for error messages

        messages.info(
            self.request,  "You have successfully registered. We will contact you in no time."
        )

        e_offer = form.save()

        name = e_offer.name
        email = e_offer.email
        about = e_offer.about

        full_message = f"""
            Received message below from {name}, {email}
            ________________________

            {about}
        """

        send_mail(
            subject="Received E-Offer",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )

        return super().form_valid(form)

    
    

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("home:contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message. We will contact you in no-time."
        )

        # Create an instance of ContactModel and save it to the database
        contact = form.save()  # This will save the form data to the ContactModel model

        name = contact.name  # Access the fields of the ContactModel instance
        email = contact.email
        about = contact.about
        

        full_message = f"""
            Received message below from {name}, {email}
            ________________________

            {about}
 
        """

        send_mail(
            subject="Received contact from contact page",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )

        return super(ContactView, self).form_valid(form)    
    
    
    
class Custom404View(View):
    def get(self, request, exception=None, *args, **kwargs):
        return render(request, '404.html', status=404)

class Custom500View(View):
    def get(self, request, *args, **kwargs):
        return render(request, '500.html', status=500)    