from django.db.models.base import Model
from rest_framework import serializers
from .models import Product

class ProductModelSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'