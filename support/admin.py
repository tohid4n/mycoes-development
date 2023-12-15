from django.contrib import admin
from .models import GeneralFAQ, ServicesFAQ, PricingFAQ, AdditionalFAQ

admin.site.register(GeneralFAQ)
admin.site.register(ServicesFAQ)
admin.site.register(PricingFAQ)
admin.site.register(AdditionalFAQ)