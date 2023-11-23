from django.contrib import admin
from .models import Offer, OfferMilestone, CommunicationPlatforms

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'timestamp')

class OfferMilestoneInline(admin.TabularInline): 
    model = OfferMilestone

@admin.register(Offer)
class OfferAdminWithInline(admin.ModelAdmin):
    inlines = [OfferMilestoneInline]

