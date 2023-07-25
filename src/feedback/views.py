from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from .forms import FeedbackForm
from .models import Feedback



class FeedbackView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'feedback.html'
    form_class = FeedbackForm
    model = Feedback

    
    def get_success_url(self):
        return reverse('feedback:feedback-view')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
