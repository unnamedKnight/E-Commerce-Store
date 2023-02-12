from django.shortcuts import get_object_or_404, render
from .models import Category, Product


# Create your views here.


def categories(request):
    """This function is context_processor. It returns all categories"""
    categories = Category.objects.all()
    return {"categories": categories}


def category_list(request, slug):
    """Detailed Category View"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "store/category_list.html", context)


def store(request):
    """lists all the products"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/store.html", context)


def product_info(request, slug):
    """Returns a product for a given slug"""
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, "store/product_info.html", context)
