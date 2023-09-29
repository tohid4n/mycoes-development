from django.shortcuts import render
from django.views import generic

class NoProjectPage(generic.TemplateView):
    template_name = 'no-project-page.html'
