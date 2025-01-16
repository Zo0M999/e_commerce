from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product


def cart(request):
    cart = Cart(request)
    products = cart.get_products()
    quantities = cart.get_quantities()
    total_sum = cart.get_total()
    return render(request, 'cart/cart.html', context={
        'title': 'Cart',
        'cart': cart,
        'products': products,
        'quantities': quantities,
        'total_sum': total_sum,
    })

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=quantity)

        return JsonResponse({
            'quantity': cart.__len__(),
        })

def cart_remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')

        cart.remove(product_id=product_id)

        return JsonResponse({
            'quantity': cart.__len__(),
        })

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        cart.update(product_id=product_id, quantity=quantity)

        return JsonResponse({
            'quantity': cart.get_quantities()[product_id],
        })

def cart_clear(request):
    ...

def checkout(request):
    ...
