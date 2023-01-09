from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.shortcuts import get_object_or_404, render

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "contact.html", context)

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)

def category(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "category.html", context)

# def product_all(request):
#     products = Item.objects .all()
#     return render(request, 'store/index.html', {'products': products})  # .objects.filter(is_active=True)


# def category(request, category_slug=None):
#     category = get_object_or_404(Item, slug=category_slug)
#     products = Item.objects.filter(category=category)
#     return render(request, 'category.html', {'category': category, 'products': products})
#
#
# def product(request):
#     product = get_object_or_404(Item, slug=slug, is_active=True)
#     return render(request, 'product.html', {'product': product})