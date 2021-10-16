from django.urls import path

from .views import  GetActiveData, PostModelData, ProductsList, UpdateActiveData , product_detail , SearchProductsView,ProductsListByCategory,products_categories_partial,GetAllData


urlpatterns = [
    path('products/', ProductsList.as_view(),name='list'),
    path('products/<productId>/<name>/',product_detail),
    path('products/search/', SearchProductsView.as_view()),
    path('products/<category_name>/', ProductsListByCategory.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial'),
    path('get-all-data/', GetAllData.as_view()),
    path('get-active-data/', GetActiveData.as_view()),
    path('update-Active-data/<int:pk>/', UpdateActiveData.as_view()),
    path('post-model/', PostModelData.as_view()),
]