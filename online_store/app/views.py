from django.shortcuts import render
from .models import Item, OrderItem, Order


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "index.html", context)