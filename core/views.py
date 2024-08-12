from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.core.mail import EmailMessage

import logging
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'core/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save()

                full_message = f"First Name: {instance.first_name}\nLast Name: {instance.last_name}\nEmail: {instance.email}\nPhone: {instance.phone}\n\n{instance.message}"

                email = EmailMessage(
                    subject=instance.subject,
                    body=full_message,
                    from_email='royal.imbau.mail@gmail.com',
                    to=['alejandro.imbau@gmail.com'],
                    reply_to=[instance.email],
                )
                email.send()
                return redirect('/contact/?submitted=True')
            except Exception as e:
                logger.error(f"Error during form submission: {e}")
                return render(request, 'core/contact.html', {'form': form, 'submission_error': True})
        else:
            logger.error(f"Form errors: {form.errors}")
            return render(request, 'core/contact.html', {'form': form})
    else:
        form = ContactMessageForm()

    return render(request, 'core/contact.html', {'form': form})


def services(request):
    return render(request, 'core/services.html')


def about(request):
    return render(request, 'core/about.html')


def gallery(request):
    return render(request, 'core/gallery.html')


def template(request):
    return render(request, 'core/template.html')
