from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailService:
    @staticmethod
    def send_email(subject , to , template_name , context):
        html_message=render_to_string(template_name , context)
        plain_message=strip_tags(html_message)
        send_mail(subject , plain_message ,'myzshop1400@gmail.com',to,html_message)