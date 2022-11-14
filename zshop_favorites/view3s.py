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


vmess://eyJhZGQiOiI2NS4yMS4yOC4xODAiLCJhaWQiOiIwIiwiaG9zdCI6IiIsImlkIjoiMDczM2E2ZmUtM2ZkZC0xMWVkLWI4NzgtMDI0MmFjMTIwMDAyIiwibmV0Ijoid3MiLCJwYXRoIjoiL2dyYXBocWwiLCJwb3J0IjoiODAiLCJwcyI6InhveG8yIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiIiLCJ2IjoiMiJ9
