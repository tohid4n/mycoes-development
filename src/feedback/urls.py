from django.urls import path
from .views import FeedbackView, FeedbackDeleteView

app_name = 'feedback'

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback-view'),
    path('<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback-delete'),
]