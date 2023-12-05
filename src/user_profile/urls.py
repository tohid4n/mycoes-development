from django.urls import  path, re_path
from .views import  OfferView, BillingView, PaypalPaymentView, PaypalPaymentSuccessView, ProfileTranscationsView

app_name = 'user_profile'

urlpatterns = [
    path('offer/', OfferView.as_view(), name="make-offer"),
    path('offers-billing/', BillingView.as_view(), name='offers-billing'),
    re_path(r'^payments/paypal/(?P<next_milestone_id>[\w-]+)/$', PaypalPaymentView.as_view(), name='paypal-payment'),
    re_path(r'^payments/paypal/success/(?P<next_milestone_id>[\w-]+)/$', PaypalPaymentSuccessView.as_view(), name='paypal-payment-success'),
    path('transctions/', ProfileTranscationsView.as_view(), name='transctions'),
]

