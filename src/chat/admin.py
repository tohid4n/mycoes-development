from django.contrib import admin
from .models import ChatMessage, AdminMessage

# Register your models here.

admin.site.register(ChatMessage)
admin.site.register(AdminMessage)
