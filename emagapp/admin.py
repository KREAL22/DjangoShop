from django.contrib import admin
from .models import Category, Brand, Product, CartItem, Cart, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'available']
    list_filter = ['available']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('title', )} 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
