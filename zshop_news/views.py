from django.shortcuts import render

# Create your views here.
def news_page(request):
    context={}
    return render(request,'news_page.html' , context)