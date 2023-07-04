from django.shortcuts import render
from django.views import generic


class ServicesHomeView(generic.TemplateView):
    template_name = 'serviceshome.html'
       
    
class FrontEndView(generic.TemplateView):
    template_name = 'front-end.html'
       

class BackEndView(generic.TemplateView):
    template_name = 'back-end.html'
    