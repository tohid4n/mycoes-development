from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()
    
    
class E_OfferModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()    
    accept = models.BooleanField()
    

   
   
    
