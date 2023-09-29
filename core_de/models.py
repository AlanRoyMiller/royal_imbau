from django.db import models
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ContactMessage_de(models.Model):

    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(validators=[EmailValidator()], blank=False)
    phone = PhoneNumberField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False)