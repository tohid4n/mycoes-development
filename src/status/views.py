from django.views import View
from django.shortcuts import render, redirect
from orders.models import Offer
from .models import ProgressBar
from .forms import ProgressBodyForm
from django.contrib.auth.mixins import LoginRequiredMixin

class StatusView(LoginRequiredMixin, View):
    def get(self, request):
        # Check if the user has made an offer
        has_made_offer = Offer.objects.filter(user=request.user).exists()

        if has_made_offer:
            # Get the status of the user's offer
            offer = Offer.objects.get(user=request.user)
            offer_status = offer.status
            

            if offer_status == 'Pending':
                # Render the template for users with a pending offer
                return render(request, 'status/pending.html')
            elif offer_status == 'Accepted':
                # Render the template for users with an accepted offer
                project_title = offer.title
                project_description = offer.description
                
                try:
                    # Get the progress bar if it exists
                    progress_bar = ProgressBar.objects.get(offer=offer)
                    bar_percentage = progress_bar.bar_precentage
                except ProgressBar.DoesNotExist:
                    # Set default values if the progress bar does not exist
                    bar_percentage = 0
                
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
        offer = Offer.objects.get(user=request.user)

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
            project_title = offer.title
        
        try:
            # Get the progress bar if it exists
            progress_bar = ProgressBar.objects.get(offer=offer)
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

    
    