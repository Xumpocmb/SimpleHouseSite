from django.urls import path
from .views import contact_message

app_name = 'contacts_app'

urlpatterns = [
    path('contact/', contact_message, name='contact'),
]
