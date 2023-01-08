from django.contrib import admin
from .models import Item, OrderItem, Order


# Register your models here.

# class Item(admin.ModelAdmin):
#     list_display = ("title", "preis")

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)

#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['price', 'stock', 'available']
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Product, ProductAdmin)