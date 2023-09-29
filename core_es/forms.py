from django import forms
from .models import ContactMessage_es

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage_es
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Asunto'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mensaje'}),
        }

