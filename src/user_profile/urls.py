from django.urls import path
from .views import BillingView, ProfileTranscationsView, OfferView

app_name = 'user_profile'

urlpatterns = [
    path('offers-billing/', BillingView.as_view(), name='profile-offers-billing'),
    path('transctions/', ProfileTranscationsView.as_view(), name='profile-transctions'),
    path('offer/', OfferView.as_view(), name="make-offer"),
]

