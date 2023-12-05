from django.contrib import admin
from user_profile.views import CustomLogoutView
from django.urls import path, include
from home.views import Custom404View, Custom500View


urlpatterns = [
    path('tohid/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('support/', include('support.urls', namespace='support')),
    path('auth/', include('magiclink.urls', namespace='magiclink')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path("cookies/", include("cookie_consent.urls")),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
]


handler404 = Custom404View.as_view()
handler500 = Custom500View.as_view()