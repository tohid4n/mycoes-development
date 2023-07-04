from django.shortcuts import render, redirect
from django.views import View
from .forms import ChatForm, AdminMessageForm
from .models import ChatMessage, AdminMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatView(LoginRequiredMixin, View):
    def get(self, request):
        chat_form = ChatForm()
        admin_message_form = AdminMessageForm()
        chats = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
        admin_messages = AdminMessage.objects.filter(chat_message__isnull=False).order_by('timestamp')
        context = {
            'chat_form': chat_form,
            'admin_message_form': admin_message_form,
            'chats': chats,
            'admin_messages':  admin_messages,
        }
        return render(request, 'chat.html', context)

    def post(self, request):
        chat_form = ChatForm(request.POST, None)
        admin_message_form = AdminMessageForm(request.POST, None)
        
        if chat_form.is_valid():
            message = chat_form.cleaned_data['message']
            ChatMessage.objects.create(user=request.user, message=message)
            return redirect('chat:chat-page')
        
        if admin_message_form.is_valid():
            message = admin_message_form.cleaned_data['message']
            chat_message = ChatMessage.objects.create(user=request.user, message=message)
            AdminMessage.objects.create(chat_message=chat_message, message=message)
            return redirect('chat:chat-page')
        
        chats = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
        admin_messages = AdminMessage.objects.filter(chat_message__isnull=False).order_by('timestamp')
        context = {
            'chat_form': chat_form,
            'admin_message_form': admin_message_form,
            'chats': chats,
            'admin_messages': admin_messages
        }
        return render(request, 'chat.html', context)

