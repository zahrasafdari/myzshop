"""toplearn_eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler400
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myZshop import settings
from .views import home_page, header, footer,about_page
import myZshop

urlpatterns = [
    path('', home_page,name='home'),
    path('about-us', about_page,name='about-us'),
    path('', include('zshop_account.urls')),
    path('', include('zshop_products.urls')),
    path('', include('zshop_contact.urls')),
    path('', include('zshop_order.urls')),
    path('', include('zshop_favorites.urls')),
    path('', include('zshop_news.urls')),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('admin/', admin.site.urls)
]

handler404='myZshop.views.handle_404_error'

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
