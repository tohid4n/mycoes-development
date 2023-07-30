from django.urls import path
from .views import HomePageView, AboutView, ContactView, SupportView, PrivacyPolicyView, TermsOfServicesView


app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('support/', SupportView.as_view(), name="support"),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name="privacy-policy"),
    path('terms-of-services/', TermsOfServicesView.as_view(), name="terms-of-services"),
]
