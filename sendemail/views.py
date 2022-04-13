from django.shortcuts import render, redirect
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_mail = request.POST['contact-mail']
        contact_message = request.POST['contact-message']
        
        #sends the email
        send_mail(
            contact_name,
            contact_message + ' from email: ' + contact_mail,
            contact_mail,
            ['cosmincosmk@gmail.com'],

        )

        return redirect('success')

    else:
        return render(request, 'sendemails/contact.html', {'page_title': "Contact"})

def success(request):

    return render(request, 'sendemails/success.html', {'page_title': "Success"})
