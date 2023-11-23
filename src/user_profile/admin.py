from django.contrib import admin
from .models import Offer, offer_milestone, CommunicationPlatforms

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'timestamp')  # Customize the fields displayed in the list view



admin.site.register(Offer, OfferAdmin)
admin.site.register(offer_milestone)
admin.site.register(CommunicationPlatforms)