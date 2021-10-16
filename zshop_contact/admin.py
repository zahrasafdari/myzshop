from zshop_contact.models import ContactUs
from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['fullname' , 'subject' , 'is_read']
    list_filter=['is_read']
    list_editable=['is_read']
    search_fields=['subject' , 'text']

admin.site.register(ContactUs,ContactAdmin)