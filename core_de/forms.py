from django import forms
from .models import ContactMessage_de

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage_de
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Vorname'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nachname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-Mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Betreff'}),
            'message': forms.Textarea(attrs={'placeholder': 'Nachricht'}),
        }
