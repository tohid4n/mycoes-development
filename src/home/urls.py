from django.urls import path
from .views import HomePageView, AboutView, ContactView


app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
]
