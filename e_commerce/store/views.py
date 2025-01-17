from django.shortcuts import render
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', context={
        'title': 'Home',
        'categories': categories,
    })


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all_products.html', context={
        'title': 'All Products',
        'products': products,
    })

def product(request, prod_id):
    product = Product.objects.get(id=prod_id)
    return render(request, 'store/product.html', context={
        'title': 'Product',
        'product': product,
    })

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', context={
        'title': 'Category',
        'category': category,
        'products': products,
    })

def about(request):
    return render(request, 'store/about.html', context={
        'title': 'About',
    })