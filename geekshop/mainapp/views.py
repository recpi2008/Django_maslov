from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title':'Главная',
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/index.html',context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html',context)

def products(request, pk=None):
    context = {
        'title':'Продукты',
        'links_menu': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context=context)

