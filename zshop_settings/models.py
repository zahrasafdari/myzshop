from django.db import models
import os

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.siteTitle}{ext}"
    return f"logo-image/{final_name}"


class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    about_us = models.TextField(null=True, blank=True)
    copy_right=models.CharField(max_length=400,null=True,blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.siteTitle
