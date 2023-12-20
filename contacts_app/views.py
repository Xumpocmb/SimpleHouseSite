from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from .models import ContactMessages
from .forms import ContactMessagesForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives


def contact_message(request):
    context = {
        'title': 'Contact Page',
    }
    if request.method == 'POST':
        form = ContactMessagesForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            ContactMessages.objects.create(name=name, email=email, message=message)
            send_email(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            messages.success(request, 'Your message has been sent.')
    else:
        form = ContactMessagesForm()
        context['form'] = form
    return render(request, 'contacts_app/contact.html', context)


def send_email(name, email, message):
    text = get_template('contacts_app/message.html')
    html = get_template('contacts_app/message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Contact Form Message'
    from_email = settings.EMAIL_HOST_USER
    text_content = text.render(context)
    html_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['x.xumpocmb@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

