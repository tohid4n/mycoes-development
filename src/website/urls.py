from django.contrib import admin
from user_profile.views import CustomLogoutView
from django.urls import path, include

urlpatterns = [
    path('tohid/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    #path('status/', include('status.urls', namespace='status')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('support/', include('support.urls', namespace='support')),
    path('auth/', include('magiclink.urls', namespace='magiclink')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('payments/', include('payments.urls')),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
]