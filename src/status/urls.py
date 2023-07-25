from django.urls import path
from .views import StatusView, CreateCheckoutSessionView, stripe_webhook, download_file

app_name = 'status'

urlpatterns = [
    path('', StatusView.as_view(), name='home'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('download/<int:offer_id>/', download_file, name='download'),
    path('cancelled/', CreateCheckoutSessionView.as_view(), name='cancel')
]
