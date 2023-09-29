from django.urls import path
from .views import NoProjectPage


app_name = 'projects'

urlpatterns = [
    path('', NoProjectPage.as_view(), name="no-project-page"),
]
