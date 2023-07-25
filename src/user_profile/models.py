from django.db import models
from django.contrib.auth.models import User

class PurchasedOffer(models.Model):
    offer = models.ForeignKey('orders.Offer', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    stripe_offer_id = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.user} - {self.offer.title}"

class DownloadFile(models.Model):
    offer = models.ForeignKey('orders.Offer', on_delete=models.CASCADE)
    file = models.FileField(upload_to='purchased/')

    def __str__(self):
        return f"{self.offer.title}"
