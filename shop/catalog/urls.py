from django.urls import path
from .views import index, product_list, add_product, phones_list

urlpatterns = [
    path('', index, name='index'),
    path('product_list/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('phones/', phones_list, name='phones_list'),
]
