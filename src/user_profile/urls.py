from django.urls import path

from .views import OrderView, TransactionsView

app_name = 'user_profile'

urlpatterns = [
    path('', OrderView.as_view(), name='profile-orders'),
    path('transactions', TransactionsView.as_view(), name='profile-transactions'),
]