
from django.contrib.auth.models import User
from django.db import models
import os
from django.db.models import Q
from zshop_products_category.models import ProductCategory

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"

class ProductsManager(models.Manager):
    def get_active_products(self):
        
        return self.get_queryset().filter(active=True)
        
    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()

        
class Product(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    price=models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    visit_count=models.IntegerField(default=0)
    favorites=models.ManyToManyField(User,related_name='favorites',default=None,blank=True)

    objects = ProductsManager()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ' , '-')}"


class ProductGallery(models.Model):
    title=models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_gallery_image_path)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.title