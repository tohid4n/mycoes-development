from django.urls import reverse
from django.views import  generic
from .models import FAQ
from django.http import JsonResponse
from django.db.models import Q


class SupportView(generic.TemplateView):
    template_name = 'support.html'
    
    
class FAQAutocompleteSearch(generic.View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('term', '')
        faqs = FAQ.objects.filter(
            Q(question__icontains=search_term) | Q(answer__icontains=search_term)
        )[:10]  # Limit to 10 results
        data = [{'id': faq.id, 'text': faq.question} for faq in faqs]
        return JsonResponse(data, safe=False)