from django.urls import reverse
from django.views import  generic
from .models import FAQ
from django.http import JsonResponse
from django.db.models import Q


class SupportView(generic.TemplateView):
    template_name = 'support.html'
    
    
class SearchFAQsView(generic.View):
    def get(self, request):
        search_term = request.GET.get('term')
        faqs = FAQ.objects.filter(question__icontains=search_term)
        faq_data = [{'question': faq.question, 'answer': faq.answer} for faq in faqs]

        return JsonResponse({'status': 200, 'data': faq_data})

    
    
