from django.urls import path, include

from .views import OrderView, TransactionsView, NoOrderView

app_name = 'user_profile'

urlpatterns = [
    path('orders', OrderView.as_view(), name='profile-home'),
    path('no-orders', NoOrderView.as_view(), name='no-orders'),
    path('transactions', TransactionsView.as_view(), name='transactions')
]