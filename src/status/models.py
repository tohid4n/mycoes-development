from django.db import models
from orders.models import Offer


class ProgressBar(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    bar_precentage = models.IntegerField()
    
    
class ProgressBody(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    preview_check = models.BooleanField(default=False)
    comment = models.TextField()
    

