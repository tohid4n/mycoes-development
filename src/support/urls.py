from django.urls import path
from .views import SupportView, SearchFAQsView

app_name = 'support'

urlpatterns = [
    path('', SupportView.as_view(), name="home"),
    path('search_faqs/', SearchFAQsView.as_view(), name='search_faqs'),

]
