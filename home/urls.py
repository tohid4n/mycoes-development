from django.urls import path
from .views import HomePageView, AboutView, ServicesView, PricingView, ContactView, E_OfferView, PrivacyPolicyView, TermsOfServicesView


app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('about/', AboutView.as_view(), name="about"),
    path('services/', ServicesView.as_view(), name="services"),
    path('pricing/', PricingView.as_view(), name="pricing"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('mycoes-offers/', E_OfferView.as_view(), name="e-offer"),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name="privacy-policy"),
    path('terms-of-services/', TermsOfServicesView.as_view(), name="terms-of-services"),
]
