from django.db import models

# Create your models here.
class ContactUs(models.Model):
    fullname=models.CharField(max_length=150)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    text=models.TextField()
    is_read=models.BooleanField()

    def __str__(self):
        return self.subject