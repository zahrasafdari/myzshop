from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from zshop_comments.forms import CreateCommentForm
from zshop_comments.models import Comment
from .models import Product, ProductGallery
from django.http import Http404
from zshop_tag.models import Tag
from zshop_products.models import ProductCategory
import itertools
from zshop_order.forms import UserNewOrderForm
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import ProductModelSeriallizer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by=6
    def get_queryset(self):
        return Product.objects.get_active_products()



class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail(request, *args, **kwargs):    
    selected_product_id = kwargs['productId']
    new_order_form=UserNewOrderForm(request.POST or None , initial={'product_id':selected_product_id})
    product_name = kwargs['name']

    product : Product= Product.objects.get_by_id(selected_product_id)
    
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    product.visit_count+=1
    product.save()

    related_products=Product.objects.get_queryset().filter(categories__product=product).distinct()
    grouped_related_products = list(my_grouper(3, related_products))

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)

    grouped_galleries = list(my_grouper(3, galleries))
    comment_form = CreateCommentForm(request.POST or None)
    if request.method=='POST':
        if comment_form.is_valid():
            name = comment_form.cleaned_data.get('name')
            email = comment_form.cleaned_data.get('email')
            message = comment_form.cleaned_data.get('message')
            new_comment=Comment.objects.create(product=product ,name=name, email=email,message=message)
            new_comment.save()
            # todo : show user a success message
        

    comments=Comment.objects.all().filter(product=product)
    context = {
        'product': product,
        'galleries': grouped_galleries,
        'related_products':grouped_related_products,
        'new_order_form':new_order_form,
        'comment':comments,
        'comments_form':comment_form
    }

    return render(request, 'products/product_detail.html', context)

class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()
    
def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)


class GetAllData(APIView):
    def get(self, request):
        query = Product.objects.all().order_by('-id')
        serializers = ProductModelSeriallizer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

class GetActiveData(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = Product.objects.filter(active=True)
        serializer = ProductModelSeriallizer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateActiveData(APIView):
    def get(self, request, pk):
        query = Product.objects.get(pk=pk)
        serializer = ProductModelSeriallizer(query, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Product.objects.get(pk=pk)
        serializer = ProductModelSeriallizer(query, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostModelData(APIView):
    def post(self, request):
        serializer = ProductModelSeriallizer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
