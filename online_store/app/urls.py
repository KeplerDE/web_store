from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('product/', views.product, name='product'),
    path('category', views.category, name='category'),
    # path('<slug:slug>', views.product, name='product'),
    # path('search/<slug:category_slug>/', views.category, name='category'),


]