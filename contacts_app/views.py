from django.shortcuts import render
from .models import ContactMessages
from .forms import ContactMessagesForm


def contact_message(request):
    context = {
        'title': 'Contact Page',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessages.objects.create(name=name, email=email, message=message)
    else:
        form = ContactMessagesForm()
        context['form'] = form
    return render(request, 'contacts_app/contact.html', context)
