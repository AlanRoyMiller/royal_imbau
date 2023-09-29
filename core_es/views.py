from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.core.mail import EmailMessage


def home(request):
    return render(request, 'core_es/inicio.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        # check if the form is valid and clean the data
        if form.is_valid():
            print("Form is valid")
            
            # save the form
            instance = form.save()

            # prepare the message
            full_message = f"First Name: {instance.first_name}\nLast Name: {instance.last_name}\nEmail: {instance.email}\nPhone: {instance.phone}\n\n{instance.message}"
            
            # send the email
            email = EmailMessage(
                subject=instance.subject,
                body=full_message,
                from_email='royal.imbau.mail@gmail.com', # This is your sending Gmail address
                to=['alejandro.imbau@gmail.com'],  # Your Gmail address where you want to receive the form details
                reply_to=[instance.email],  # This allows you to reply directly to the person who filled out the form
            )
            email.send()
            
            return redirect('/es/contacto/?submitted=True') 
        else:
            print(form.errors)  # Print form errors if the form is not valid
            return render(request, 'core_es/contacto.html', {'form': form})
    else:
        form = ContactMessageForm() 

    form_submitted = 'submitted' in request.GET
    return render(request, 'core_es/contacto.html', {'form': form}) 


    


def services(request):
    return render(request, 'core_es/servicios.html')

def about(request):
    return render(request, 'core_es/sobre-nosotros.html')

def gallery(request):
    return render(request, 'core_es/galeria.html')

def template(request):
    return render(request, 'core_es/template.html')

