from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from payments.models import BasePayment
from payments import PurchasedItem
from payments.models import BasePayment
from django.urls import reverse
    
    
class OfferMilestone(models.Model):
    id = models.AutoField(primary_key=True)
    milestone_number = models.PositiveIntegerField()
    ammount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)
    paid = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='milestones')
    
    class Meta:
        unique_together = ['offer', 'milestone_number']

    

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    timeline = models.CharField(max_length=70)
    budget = models.CharField(max_length=70)
    attached_files = models.FileField(upload_to='uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
       
    
    
class CommunicationPlatforms(models.Model):
    platform = models.URLField(max_length=100, null=True, blank=True)   
    platform_name = models.CharField(max_length=50, null=True, blank=True)   
    
    


class Payment(BasePayment):
    def get_failure_url(self):
        return reverse("user_profile:payment-success")

    def get_success_url(self):
        return reverse("user_profile:payment-failure")

    def get_purchased_items(self):
        yield PurchasedItem(
            name=self.description,
            price=self.total,
            currency=self.currency,
            sku="BSKV",
            quantity=1,
        )


    
    
