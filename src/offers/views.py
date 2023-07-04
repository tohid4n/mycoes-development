from django.shortcuts import render
from django.views import View

from django.views.generic import FormView
from .forms import ContactForm
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated


# class MakeAnOfferView(FormView):
#     template_name = 'make-offer.html'
#     form_class = ContactForm
#     success_url = '/contact/success/'
#     permission_classes = [IsAuthenticated]
    
#     def form_valid(self, form):
#         serializer = ContactSerializer(data=form.cleaned_data)
#         if serializer.is_valid():
#             serializer.save()
#             return super().form_valid(form)
#         else:
#             errors = serializer.errors
#             return self.form_invalid(form)
    



class MakeAnOfferView(View):
    def get(self, request):
        return render(request, 'make-offer.html')