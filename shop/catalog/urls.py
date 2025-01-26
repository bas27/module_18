from django.urls import path
from .views import index, product_list, add_product, phones_list, home, contact_view, feedback_view, \
    products_by_category, disconted_products

urlpatterns = [
    path('', index, name='index'),
    path('product_list/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('phones/', phones_list, name='phones_list'),
    path('home/', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('feedback/', feedback_view, name='feedback_form'),
    path('category/<str:category_name>', products_by_category, name='products_by_category'),
    path('discounts', disconted_products, name='disconted_products'),
]
