from django.contrib import admin
from .models import Offer, OfferMilestone

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'timestamp')
    
    def user_name(self, obj):
        return obj.user.username
    user_name.short_description = 'User'
    user_name.admin_order_field = 'user__username'

class OfferMilestoneInline(admin.TabularInline): 
    model = OfferMilestone
    ordering = ('created_at',)

    
@admin.register(Offer)
class OfferAdminWithInline(admin.ModelAdmin):
    inlines = [OfferMilestoneInline]
    list_display = ('title', 'user_name', 'timestamp')
    search_fields = ['title', 'user__username']   
    
    def user_name(self, obj):
        return obj.user.username
    user_name.short_description = 'User'
    user_name.admin_order_field = 'user__username'  
    
    
