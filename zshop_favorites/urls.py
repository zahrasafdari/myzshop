from zshop_favorites.views import favorite_add
from django.urls import path
from . import views

app_name='zshop_favorites'
urlpatterns = [
    path('<int:id>/fav/', views.favorite_add, name='favorite'),
]