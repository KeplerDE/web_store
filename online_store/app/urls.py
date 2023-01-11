from django.urls import path
from . import views
from .views import HomeView, ItemDetailView
app_name = 'app'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', ItemDetailView.as_view(), name='details'),
    path('category/', views.category, name='category'),

    # path('product/<slug>/', ProductView.as_view(), name='product'),
    # path('<slug:slug>', views.product, name='product'),
    # path('search/<slug:category_slug>/', views.category, name='category'),    # path('product/', views.product, name='product'),

    # path('<slug:slug>', views.product_detail, name='product_detail'),

]