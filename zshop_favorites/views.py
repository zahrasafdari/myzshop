from django.http.response import HttpResponseRedirect
from zshop_products.models import Product
from zshop_favorites.forms import FavoritProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

@login_required
def favorite_add(request, fav_id):
    favorite_product = get_object_or_404(Product, id=fav_id)
    if favorite_product.favorites.filter(id=request.user.id).exists():
        favorite_product.favorites.remove(request.user)
    else:
        favorite_product.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


