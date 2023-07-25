from django.db import models
from django.contrib.auth.models import User


class Offer(models.Model):
    
    FULLSTACK = 'Full stack'
    FRONTEND = 'Front-end'
    BACKEND = 'Back-end'
    
    DEVELOPMENT_CHOICES = (
        (FULLSTACK, 'Full stack'),
        (FRONTEND, 'Front-end'),
        (BACKEND, 'Back-end'),
    )

    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    STATUS_CHOICES = (
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateField()
    development_category = models.CharField(max_length=12, choices=DEVELOPMENT_CHOICES, default=FULLSTACK)
    budget = models.IntegerField()
    attached_files = models.FileField(upload_to='uploads/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    download_file = models.ForeignKey('user_profile.DownloadFile', on_delete=models.SET_NULL, null=True, blank=True, related_name='offer_download_files')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
   
   
    
