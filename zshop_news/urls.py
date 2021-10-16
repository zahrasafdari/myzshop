from django.urls import path
from .views import news_page

urlpatterns = [
    path('news' , news_page,name='news'),
]