from django import forms
from .models import ContactMessages


class ContactMessagesForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'rows': 5,
                                             'placeholder': 'Message'}),
        }
