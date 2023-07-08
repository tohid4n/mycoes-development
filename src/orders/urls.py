from django.urls import path
from .views import OfferView


app_name = 'orders'

urlpatterns = [
    path('', OfferView.as_view(), name="make-offer"),
]