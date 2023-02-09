from django.contrib import admin
from .models import Category, Product

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # this method doesn't produce unique slugs
    # prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("slug",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("slug",)

