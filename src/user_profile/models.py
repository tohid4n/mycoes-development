from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from payments.models import BasePayment
    
    
class OfferMilestone(models.Model):
    ammount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)
    paid = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='milestones')

    def __str__(self):
        return f"{self.id} - {self.ammount}"

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

    
    


    
    

class Payment(BasePayment):

    def get_failure_url(self) -> str:
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self) -> str:
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"
    
    
    
class CommunicationPlatforms(models.Model):
    platform = models.URLField(max_length=100, null=True, blank=True)   
    platform_name = models.CharField(max_length=50, null=True, blank=True)   
    




    
    
