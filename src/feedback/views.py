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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.all()  # Retrieve all feedbacks from the database
        feedback_count = feedbacks.count()  # Count the number of feedbacks
        context['feedbacks'] = feedbacks
        context['feedback_count'] = feedback_count
        return context
    

class FeedbackDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Feedback
    template_name = 'feedback.html' 
    
    def get_success_url(self):
        return reverse('feedback:feedback-view')