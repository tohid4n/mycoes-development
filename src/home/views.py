from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.views import  generic
from .forms import ContactForm


class HomePageView(generic.TemplateView):
    template_name = 'home-page.html'
    

class AboutView(generic.TemplateView):
    template_name = 'about.html'
    
  
class SupportView(generic.TemplateView):
    template_name = 'support.html'   
    
class PrivacyPolicyView(generic.TemplateView):
    template_name = 'privacy-policy.html'   
    
class TermsOfServicesView(generic.TemplateView):
    template_name = 'terms-of-services.html'            
   

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    
    def get_success_url(self):
        return reverse("home:contact")
    
    def form_valid(self, form):
        messages.info(
           self.request, "Thanks for getting in touch. We have received your message. We will contact you in no-time."
        )
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        topic = form.cleaned_data['topic']
        message = form.cleaned_data['message']
       
        full_message = f"""
            Received message below from {full_name}, {email}
            ________________________
            
            {topic}  
            
              
            {message}
            """
            
        send_mail(
            subject="Received contact from contact page",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )    
        return super(ContactView, self).form_valid(form)
       


