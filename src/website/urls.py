from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tohid/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('status/', include('status.urls', namespace='status')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('accounts/', include('allauth.urls')),
    path('order/', include('orders.urls', namespace='orders')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('support/', include('support.urls', namespace='support')),
]