from django import views
from django.urls import path
from .views import  OfferView, BillingView, CreatePaymentView, PaymentDetailsView, PaymentSuccessView, PaymentFailureView, ProfileTranscationsView

app_name = 'user_profile'

urlpatterns = [
    path('offer/', OfferView.as_view(), name="make-offer"),
    path('offers-billing/', BillingView.as_view(), name='profile-offers-billing'),
    path("create-payment/", CreatePaymentView.as_view(), name="create-payment"),
    path("payment-details/<int:payment_id>/", PaymentDetailsView.as_view(), name="payment-details"),
    path("payment-success/", PaymentSuccessView.as_view(), name="payment-success"),
    path( "payment-failure/", PaymentFailureView.as_view(), name="payment-failure"),
    path('transctions/', ProfileTranscationsView.as_view(), name='profile-transctions'),
]

