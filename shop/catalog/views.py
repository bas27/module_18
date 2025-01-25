from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.views import View

from .models import Product

# products = [
#     {'id': 1, 'name': 'Смартфон Samsung Galaxy', 'category': 'телефоны', 'price': 15000},
#     {'id': 2, 'name': 'Планшет Apple iPad', 'category': 'планшеты', 'price': 45000},
#     {'id': 3, 'name': 'Наушники Sony WH-1000XM4', 'category': 'аксессуары', 'price': 25000},
#     {'id': 4, 'name': 'Ноутбук Dell XPS 13', 'category': 'ноутбуки', 'price': 95000},
#     {'id': 5, 'name': 'Смарт-часы Xiaomi Mi Band', 'category': 'аксессуары', 'price': 3000},
# ]


def add_product(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        # Добавляем новый товар в список
        product = {'id': len(products) + 1, 'name': name, 'category': category, 'price': price}
        products.append(product)
        # Перенаправляем на список товаров
        return redirect('product_list')  # Имя маршрута списка товаров
    # Если GET-запрос, отображаем форму
    return render(request, 'catalog/add_product.html')

# def product_list(request):
#     category = request.GET.get('category')
#     if category:
#         filtered_products = [product for product in products if product['category'] == category]
#     else:
#         filtered_products = products
#     return render(request,
#                   'catalog/product_list.html',
#                   {'products': filtered_products})


def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'catalog/product_list.html', {'products': products})


def index(request):
    products = [
        {"name": "Смартфон", "price": 15000},
        {"name": "Ноутбук", "price": 55000},
        {"name": "Планшет", "price": 25000},
    ]
    return render(request,
                  'catalog/index.html',
                  {"products": products})


class IndexView(View):

    def get(self, request):
        return HttpResponse("Добро пожаловать в интернет-магазин!")

    def post(self, request):
        return HttpResponse("Данные отправлены.")


class ProductList(View):
    def get(self, request):
        product_items = "<br>".join([f"{p['name']}: {p['price']}руб." for p in products])
        return HttpResponse(product_items)
