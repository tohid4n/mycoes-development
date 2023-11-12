from django.db import models
from django.contrib.auth.models import User
# from random import choice

# # setting color to the profile background
# COLOR_CHOICES = [
#     ('Brown', 'Brown'),
#     ('Blue', 'Blue'),
#     ('Gray', 'Gray'),
#     ('Green', 'Green'),
#     ('Purple', 'Purple'),
#     ('Yellow', 'Yellow'),
# ]

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='Gray')

#     def __str__(self):
#         return self.user.username

#     def assign_specific_color_to_user_profile(UserProfile):
#         color = choice(COLOR_CHOICES)[0]  # Choose a random color from the choices
#         UserProfile.color = color
#         UserProfile.save()
        
        
    
class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateField()
    budget = models.IntegerField()
    attached_files = models.FileField(upload_to='uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    

# class PurchasedOffer(models.Model):
#     offer = models.ForeignKey('Offer', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     paid = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     stripe_offer_id = models.CharField(max_length=255)
    

#     def __str__(self):
#         return f"{self.user} - {self.offer.title}"

# class DownloadFile(models.Model):
#     offer = models.ForeignKey('Offer', on_delete=models.CASCADE)
#     file = models.FileField(upload_to='purchased/')

#     def __str__(self):
#         return f"{self.offer.title}"



