from django.urls import path
from .views import MakeAnOfferView

app_name = 'offers'

urlpatterns = [
    path('', MakeAnOfferView.as_view(), name='make-an-offer')
]