from django.db import models
from uuslug import uuslug

# auto slug field is a django package that slugify fields uniquely and automatically

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)


# - when we add editable=false in a model field
# -  it will hide that field from django admin


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # uuslug uniquely slugify model fields
        self.slug = uuslug(self.title, instance=self)
        super(Product, self).save(*args, **kwargs)
