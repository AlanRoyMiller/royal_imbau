from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        labels = {
            'first_name': _("First Name"),
            'last_name': _("Last Name"),
            'email': _("Email"),
            'phone': _("Phone"),
            'subject': _("Subject"),
            'message': _("Message"),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _("First Name")}),
            'last_name': forms.TextInput(attrs={'placeholder': _("Last Name")}),
            'email': forms.EmailInput(attrs={'placeholder': _("Email")}),
            'phone': forms.TextInput(attrs={'placeholder': _("Phone")}),
            'subject': forms.TextInput(attrs={'placeholder': _("Subject")}),
            'message': forms.Textarea(attrs={'placeholder': _("Message")}),
        }