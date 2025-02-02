from django.urls import path
from .views import product_list, add_product, phones_list, home, contact_view, feedback_view, \
    products_by_category, disconted_products, product_list_api, category_list_api, product_reviews, review_list_api

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('phones/', phones_list, name='phones_list'),
    path('category/<str:category_name>', products_by_category, name='products_by_category'),
    path('discounts', disconted_products, name='disconted_products'),
    path('contact/', contact_view, name='contact'),
    path('feedback/', feedback_view, name='feedback_form'),
    path('api/categories/', category_list_api, name='category_list_api'),
    path('api/products/', product_list_api, name='product_list_api'),
    path('api/products/<int:product_id>/reviews', review_list_api, name='review_list_api'),
    path('products/<int:product_id>/reviews', product_reviews, name='product_reviews'),
    path('add_product/', add_product, name='add_product'),

]
