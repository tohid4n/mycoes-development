from django.views import generic
from .models import GeneralFAQ, ServicesFAQ, PricingFAQ, AdditionalFAQ

class SupportView(generic.TemplateView):
    template_name = 'support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['general_faqs'] = GeneralFAQ.objects.all() 
        context['services_faqs'] = ServicesFAQ.objects.all()
        context['pricing_faqs'] = PricingFAQ.objects.all() 
        context['additional_faqs'] = AdditionalFAQ.objects.all() 
        return context
    
    


    
    
