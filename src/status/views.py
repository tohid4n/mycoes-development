import stripe
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.views import generic, View
from django.shortcuts import render, redirect
from orders.models import Offer
from .models import ProgressBar
from user_profile.models import PurchasedOffer, DownloadFile
from .forms import ProgressBodyForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import FileResponse



import mimetypes
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404



stripe.api_key = settings.STRIPE_SECRET_KEY

class StatusView(LoginRequiredMixin, View):
    def get(self, request):
        # Check if the user has made an offer
        offers = Offer.objects.filter(user=request.user).order_by('-timestamp')
        has_made_offer = offers.exists()

        if has_made_offer:
            # Get the latest offer made by the user
            latest_offer = offers.first()
            offer_status = latest_offer.status
           
            print(f"Offer status: {offer_status}")

            if offer_status == 'Pending':
                # Render the template for users with a pending offer
                return render(request, 'status/pending.html')
            elif offer_status == 'Accepted':
                # Render the template for users with an accepted offer
                project_title = latest_offer.title
                project_description = latest_offer.description
                project_timestamp = latest_offer.timestamp
                project_budget = latest_offer.budget
                
                try:
                    # Get the purchased offer if it exists
                    purchased_offer = PurchasedOffer.objects.get(offer=latest_offer, user=request.user)
                    

                    context_purchased = {
                        'purchased_offer': purchased_offer,
                        'project_id': latest_offer.id,
                        'project_title': project_title,
                        'project_description': project_description,
                        'project_timestamp': project_timestamp
                    }

                    return render(request, 'paid.html', context_purchased)
                except PurchasedOffer.DoesNotExist:
                    # If the purchased offer does not exist, proceed to check progress or render default template
                    pass
                
                try:
                    # Get the progress bar if it exists
                    progress_bar = ProgressBar.objects.get(offer=latest_offer)
                    bar_percentage = progress_bar.bar_precentage
                except ProgressBar.DoesNotExist:
                    # Set default values if the progress bar does not exist
                    bar_percentage = 0
                    
                context_bar = {
                    'project_title': project_title,
                    'project_id': latest_offer.id,
                    'project_description': project_description,
                    'project_timestamp': project_timestamp,
                    'project_budget': project_budget,
                    'bar_percentage': bar_percentage,
                }
                    
                if bar_percentage == 100:
                    # Render the payment.html template
                    return render(request, 'payment.html', context_bar)    
                
                # Get the form for the progress update
                form = ProgressBodyForm()
    
                # Pass the project title and bar percentage as context variables
                context = {
                    'project_title': project_title,
                    'project_description': project_description,
                    'bar_percentage': bar_percentage,
                    'form': form,
                } 
                
                return render(request, 'progress.html', context)
            
            elif offer_status == 'Rejected':
                # Render the template for users with a rejected offer
                return render(request, 'status/rejected.html')
            else:
                # Render a default template if the offer status is not recognized
                return render(request, 'status/no-offermade.html')
        else:
            # Render the template for users who have not made an offer
            return render(request, 'status/no-offermade.html')
    
    def post(self, request):
        # Retrieve the offer for the logged-in user
        offers = Offer.objects.filter(user=request.user).order_by('-timestamp')
        has_made_offer = offers.exists()

        if has_made_offer:
            # Get the latest offer made by the user
            latest_offer = offers.first()
            offer = get_object_or_404(Offer, user=request.user, id=latest_offer.id)

            # Process the form submission
            form = ProgressBodyForm(request.POST, initial={'offer': offer.pk})
            if form.is_valid():
                progress_body = form.save(commit=False)
                progress_body.offer = offer
                progress_body.save()
                return redirect('status:home')
            else:
                # Handle form errors
                # Retrieve the project title
                project_title = latest_offer.title
            
            try:
                # Get the progress bar if it exists
                progress_bar = ProgressBar.objects.get(offer=latest_offer)
                bar_percentage = progress_bar.bar_precentage
            except ProgressBar.DoesNotExist:
                # Set default values if the progress bar does not exist
                bar_percentage = 0
                
            # Pass the project title, bar percentage, and form as context variables
            context = {
                'project_title': project_title,
                'bar_percentage': bar_percentage,
                'form': form,
            }
            return render(request, 'progress.html', context)
        else:
            # Render the template for users who have not made an offer
            return render(request, 'status/no-offermade.html')
        
class CancelView(generic.TemplateView):
    template_name = 'cancelled.html'


class CreateCheckoutSessionView(generic.View):
    def post(self, request, *args, **kwargs):
        offer_id = self.kwargs['pk']
        offer = get_object_or_404(Offer, user=request.user, id=offer_id)
        #purchased_offer = PurchasedOffer.objects.create(user=request.user,  offer=offer) 
        #Convert budget to cents
        unit_amount_cents = int(offer.budget * 100)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': offer.title,
                    },
                    'unit_amount': unit_amount_cents, 
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/status/',
            cancel_url='http://127.0.0.1:8000/status/canceled',
            metadata={
                'offer_id': str(offer.id),
            })
        PurchasedOffer.objects.create(user=request.user,  offer=offer, stripe_offer_id=session['id']) 
        return redirect(session.url, code=303)

 

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = event['data']['object']['id']
        customer_email = session['customer_details']['email']
        
    
        purchased_offer = PurchasedOffer.objects.filter(stripe_offer_id=session_id).first()
        
        if purchased_offer:
            purchased_offer.paid = True
            purchased_offer.save()
        
        
        html_message = render_to_string('emails/paid.html')
        send_mail(
            subject="Successfully paid",
            message=strip_tags(html_message),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[customer_email],
            html_message=html_message
        )

    return HttpResponse(status=200)







# class CreateCheckoutSessionView(generic.View):
#     def post(self, request, *args, **kwargs):
#         offer_id = self.kwargs['pk']
#         offer = get_object_or_404(Offer, user=request.user, id=offer_id)
#         #Convert budget to cents
#         unit_amount_cents = int(offer.budget * 100)
#         session = stripe.checkout.Session.create(
#             line_items=[{
#                 'price_data': {
#                     'currency': 'usd',
#                     'product_data': {
#                         'name': offer.title,
#                     },
#                     'unit_amount': unit_amount_cents, 
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url='http://127.0.0.1:8000/status/',
#             cancel_url='http://127.0.0.1:8000/status/canceled',
#             metadata={
#                 'offer_id': str(offer.id),
#             })
        
#         return redirect(session.url, code=303)

 

# @csrf_exempt
# def stripe_webhook(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)

#     if event['type'] == 'checkout.session.completed':
        
        
#         session = event['data']['object']['id']
#         session_id = event['data']['object']['id']
#         offer_id = session['metadata']['offer_id']
#         customer_email = session['customer_details']['email']

#         offer = get_object_or_404(Offer, id=offer_id)
            
#         purchased_offer = PurchasedOffer.objects.create(user=request.user,  offer=offer) 
#         purchased_offer.stripe_offer_id = session_id
#         purchased_offer.save()   
#         # Send an email or perform any other actions you want
#         # For example, sending an email to the user confirming the purchase
#         html_message = render_to_string('emails/paid.html', {'offer': offer})
#         send_mail(
#             subject="Successfully paid",
#             message=strip_tags(html_message),
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[customer_email],
#             html_message=html_message
#         )

#     return HttpResponse(status=200)




def download_file(request, offer_id):
    purchased_offer = get_object_or_404(PurchasedOffer, offer_id=offer_id, user=request.user)

    # Check if the purchased_offer has an associated DownloadFile
    try:
        download_file = DownloadFile.objects.get(offer=purchased_offer.offer)
    except DownloadFile.DoesNotExist:
        return HttpResponse("The file associated with this offer does not exist.", status=404)

    if request.user.is_authenticated:
        file = download_file.file.open(mode='rb')  # Access the file attribute of the DownloadFile
        filename = download_file.file.name  # Get the file name from the DownloadFile
        content_type, _ = mimetypes.guess_type(filename)
        response = FileResponse(file)
        response['Content-Type'] = content_type or 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename={filename}'
        return response

    return HttpResponse("You are not authorized to access this file.", status=403)
