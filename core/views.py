from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.core.mail import EmailMessage
from django.urls import reverse


import logging

logger = logging.getLogger(__name__)


def home(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if not form.is_valid():
            logger.warning("Contact form invalid: %s", form.errors)
            return render(request, 'core/home.html', {
                'form': form,
            })

        # form is valid
        try:
            instance = form.save()

            full_message = (
                f"First Name: {instance.first_name}\n"
                f"Last Name:  {instance.last_name}\n"
                f"Email:      {instance.email}\n"
                f"Phone:      {instance.phone}\n\n"
                f"{instance.message}"
            )

            email = EmailMessage(
                subject=instance.subject,
                body=full_message,
                from_email='royal.imbau.mail@gmail.com',
                to=['alejandro.imbau@gmail.com'],
                reply_to=[instance.email],
            )
            email.send()
            logger.info("Email sent, about to redirect to home with submitted flag")

            # single, canonical redirect on success:
            return redirect(f"{reverse('home')}?submitted=True")

        except Exception as e:
            logger.error("Error sending email", exc_info=True)
            return render(request, 'core/home.html', {
                'form': form,
                'submission_error': True,
                'error_message': str(e),
            })

    # GET (or after redirect)
    form = ContactMessageForm()
    form_submitted = 'submitted' in request.GET
    return render(request, 'core/home.html', {
        'form': form,
        'form_submitted': form_submitted,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        # check if the form is valid and clean the data
        if form.is_valid():
            logger.info("Form is valid")

            # save the form
            try:
                instance = form.save()

                # prepare the message
                full_message = (
                    f"First Name: {instance.first_name}\n"
                    f"Last Name: {instance.last_name}\n"
                    f"Email: {instance.email}\n"
                    f"Phone: {instance.phone}\n\n"
                    f"{instance.message}"
                )

                # send the email
                email = EmailMessage(
                    subject=instance.subject,
                    body=full_message,
                    from_email='royal.imbau.mail@gmail.com',  # This is your sending Gmail address
                    to=['alejandro.imbau@gmail.com'],  # Your Gmail address where you want to receive the form details
                    reply_to=[instance.email],  # This allows you to reply directly to the person who filled out the form
                )
                email.send()

                logger.info("Email sent successfully")
            except Exception as e:
                logger.error(f"Error during form submission: {e}")
                return render(request, 'core/home.html', {'form': form, 'submission_error': True})

            return redirect('/home/?submitted=True')
        else:
            logger.error(f"Form errors: {form.errors}")  # Log form errors if the form is not valid
            return render(request, 'core/home.html', {'form': form})
    else:
        form = ContactMessageForm()

    form_submitted = 'submitted' in request.GET
    return render(request, 'core/home.html', {'form': form})



def services(request):
    return render(request, 'core/services.html')


def about(request):
    return render(request, 'core/about.html')


def gallery(request):
    return render(request, 'core/gallery.html')


def template(request):
    return render(request, 'core/template.html')
