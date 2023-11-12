import random
import string
from django.db import models

def generate_short_id():
    while True:
        length = random.randint(4, 8)
        characters = string.ascii_letters + string.digits
        generated_id = ''.join(random.choice(characters) for i in range(length))
        if generated_id:
            return generated_id


class GeneralFAQ(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=generate_short_id, editable=False)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link_to = models.CharField(max_length=100, blank=True, null=True)
    link_to_text = models.CharField(max_length=20,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.question
    
class ServicesFAQ(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=generate_short_id, editable=False)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link_to = models.CharField(max_length=100, blank=True, null=True)
    link_to_text = models.CharField(max_length=20,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.question
    
    
class PricingFAQ(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=generate_short_id, editable=False)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link_to = models.CharField(max_length=100, blank=True, null=True)
    link_to_text = models.CharField(max_length=20,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.question
    
    
class AdditionalFAQ(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=generate_short_id, editable=False)
    question = models.CharField(max_length=255)
    answer = models.TextField()  
    link_to = models.CharField(max_length=100, blank=True, null=True)
    link_to_text = models.CharField(max_length=20,blank=True, null=True)  
    
    def __str__(self) -> str:
        return self.question        

