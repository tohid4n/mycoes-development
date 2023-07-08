from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'input_classes_chat_message',
                'placeholder': 'Enter your message',
                'rows': 1,
            }
        )
    )
    
class AdminMessageForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'input_classes_chat_message',
                'placeholder': 'Enter your message',
                'rows': 1,
            }
        )
    )