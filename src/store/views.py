from django.shortcuts import render
from .models import Category, Product


# Create your views here.


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def store(request):
    return render(request, "store/store.html")
