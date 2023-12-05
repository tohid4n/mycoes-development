import uuid
from django.db import models
from django.contrib.auth.models import User
    
    
class OfferMilestone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    milestone_number = models.PositiveIntegerField()
    ammount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)
    paid = models.BooleanField(default=False)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='milestones')
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    
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
    
 