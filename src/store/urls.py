from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("product/<slug:slug>", views.product_info, name="product_info"),
    # the following url is for detail category view
    path("search/<slug:slug>", views.category_list, name="category_list"),
]
