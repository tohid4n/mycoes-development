from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from .models import Offer
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class OfferAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'status' in form.changed_data:
            new_status = form.cleaned_data['status']
            
            obj.status = new_status
            obj.save()

            # Check the new status and send the appropriate email
            if new_status == Offer.ACCEPTED:
                # Render the HTML template
                html_message = render_to_string('emails/accepted_offer.html', {'offer': obj})

                # Send the email with HTML content
                send_mail(
                    subject="Accepted offer",
                    message=strip_tags(html_message),  # Use the plain text version as the fallback
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[obj.user.email],
                    html_message=html_message
                )
                return redirect('status:home')
            elif new_status == Offer.REJECTED:
                # Render the HTML template
                html_message = render_to_string('emails/rejected_offer.html', {'offer': obj})

                # Send the email with HTML content
                send_mail(
                    subject="Rejected offer",
                    message=strip_tags(html_message),  # Use the plain text version as the fallback
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[obj.user.email],
                    html_message=html_message
                )
                return redirect('status:home')

        return super().save_model(request, obj, form, change)

admin.site.register(Offer, OfferAdmin)



