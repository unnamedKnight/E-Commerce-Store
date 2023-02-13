from django.shortcuts import render, get_object_or_404

from store.models import Product
from .cart import Cart

# Create your views here.


def cart_summary(request):
    return render(request, 'cart/cart-summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)


def cart_update(request):
    pass


def cart_delete(request):
    pass
