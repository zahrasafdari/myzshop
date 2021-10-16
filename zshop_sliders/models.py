from django.db import models
import os
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sliders/{final_name}"


class Slider(models.Model):
    title=models.CharField(max_length=150)
    link=models.URLField(max_length=200)
    description=models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


    
    def __str__(self):
        return self.title