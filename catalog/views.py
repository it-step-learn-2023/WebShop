from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    all_categorys = Category.objects.all()
    all_producers = Producer.objects.all()
    #

    return render(request, 'catalog/index.html', context={
        'title': 'Катaлог',
        'page' : 'index',
        'app' : 'catalog',
        'all_products' : all_products,
        'all_categorys' : all_categorys,
        'all_producers' : all_producers,        
    })
