from django.shortcuts import get_object_or_404
from .models import OfferMilestone
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


            
@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        milestone = get_object_or_404(OfferMilestone, id=ipn.invoice)
        
        if OfferMilestone.total_cost() == ipn.mc_gross:
            milestone.transaction_id = ipn.txn_id
            milestone.transaction_date = ipn.payment_date
            milestone.paid = True  
            milestone.save()            