from django.db import models
from zshop_products.models import Product


# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=150, blank=True,null=True)
    email=models.EmailField(max_length=200, blank=True,null=True)
    message=models.TextField(blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    product=models.ForeignKey(Product , on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name