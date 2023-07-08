from django.shortcuts import render
from django.views import  generic
  

class NoOrderView(generic.TemplateView):
    template_name = 'no-order.html'
    
    
class OrderView(generic.TemplateView):
    template_name = 'orders.html'
        

class TransactionsView(generic.TemplateView):
    template_name = 'transactions.html'            