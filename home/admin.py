from django.contrib import admin
from .models import Category, Land, Product, Order, OrderItem, Search,ProductsImages

# Register your models here.


admin.site.register(Land)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Search)
admin.site.register(ProductsImages)

