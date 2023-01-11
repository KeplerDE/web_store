from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Item
    template_name = "home.html"                  # перекодили в generic

class ItemDetailView(DetailView):
    model = Item                           # тут нужно использовать DetailView, но URL без slug не рендерит
    template_name = "product_detail.html"     #  Generic detail view BookDetailView must be called with either an object pk or a slug in the URLconf




def category(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "category.html", context)




# def product(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "product_detail.html", context)



# def product(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "product_detail.html", context)



# def product_all(request):
#     products = Item.objects .all()
#     return render(request, 'store/home.html', {'products': products})  # .objects.filter(is_active=True)


# def category(request, category_slug=None):
#     category = get_object_or_404(Item, slug=category_slug)
#     products = Item.objects.filter(category=category)
#     return render(request, 'category.html', {'category': category, 'products': products})
#
#
# def product(request):
#     product = get_object_or_404(Item, slug=slug, is_active=True)
#     return render(request, 'product_detail.html', {'product': product})