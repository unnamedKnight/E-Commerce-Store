from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .cart import Cart

# Create your views here.


def cart_summary(request):
    return render(request, "cart/cart-summary.html")


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)

        return JsonResponse(
            {
                "product_quantity": cart.__len__(),
            }
            # note: the alternative of doing the above operation
            # response = JsonResponse(
            #     {
            #         "the product is called:": product.title,
            #         "Product quantity is: ": product_quantity,
            #     }
            # )
        )

        # return response


def cart_update(request):
    pass


def cart_delete(request):
    pass
