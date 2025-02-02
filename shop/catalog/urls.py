from django.urls import path
from .views import product_list, add_product, phones_list, home, contact_view, feedback_view, \
    products_by_category, disconted_products, product_list_api, category_list_api

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('phones/', phones_list, name='phones_list'),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('feedback/', feedback_view, name='feedback_form'),
    path('category/<str:category_name>', products_by_category, name='products_by_category'),
    path('discounts', disconted_products, name='disconted_products'),
    path('api/products/', product_list_api, name='product_list_api'),
    path('api/categories/', category_list_api, name='category_list_api'),
]
