from django.urls import path
from .views import ServicesHomeView, FrontEndView, BackEndView

app_name = 'services'

urlpatterns = [
    path('', ServicesHomeView.as_view(), name='home'),
    path('front-end/', FrontEndView.as_view(), name='front-end'),
    path('back-end/', BackEndView.as_view(), name='back-end'),
]