from django.shortcuts import render
from .models import ContactMessages
from .forms import ContactMessagesForm
from django.contrib import messages


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
            messages.success(request, 'Your message has been sent.')
    else:
        form = ContactMessagesForm()
        context['form'] = form
    return render(request, 'contacts_app/contact.html', context)
