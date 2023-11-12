from django.urls import path
from .views import PricingView, OfferView

app_name = 'user_profile'

urlpatterns = [
    path('', PricingView.as_view(), name='profile'),
    path('offer/', OfferView.as_view(), name="make-offer"),
]

