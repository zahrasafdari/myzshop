from zshop_contact.views import contact_page
from django.urls import path
from .views import contact_page

urlpatterns = [
    path('contact-us' , contact_page,name='contact-us'),
]