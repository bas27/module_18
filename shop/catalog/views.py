from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomContactForm, FeedbackForm
from .models import Product, Category

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialaizers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        # Получаем все товары из базы данных
        products = Product.objects.all()
        # Сериализуем данные
        serializer = ProductSerializer(products, many=True)
        # Возвращаем JSON-ответ
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def disconted_products(request):
    # Фильтруем товары по цене
    products = Product.objects.filter(price__lt=100000)
    return render(request,
                  'catalog/discounted_products.html',
                  {'products': products})


def products_by_category(request, category_name):
    # Фильтруем товары по названию категории
    products = Product.objects.filter(category__name=category_name)
    return render(request,
                  'catalog/products_by_category.html',
                  {'category_name': category_name, 'products': products})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных
            print(form.cleaned_data)
            return render(request, 'catalog/feedback_success.html')
    else:
        form = FeedbackForm()

    return render(request, 'catalog/feedback_form.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = CustomContactForm(request.POST)
        if form.is_valid():
            # Если форма валидна, обрабатываем данные
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Здесь можно отправить сообщение по email или сохранить в базу данных
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    else:
        # GET-запрос, создаём пустую форму
        form = CustomContactForm()

    return render(request, 'catalog/contact.html', {'form': form})


def home(request):
    #  Получаем все категории
    categories = Category.objects.all()
    return render(request, 'catalog/home.html', {'categories': categories})


def phones_list(request):
    products = Product.objects.filter(category__name='Телефоны')
    return render(request, 'catalog/phones_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        print(name, category, price)
        cat = Category.objects.get_or_create(name=category)
        # Добавляем новый товар в список
        # product = {'name': name, 'category': category, 'price': price}
        Product.objects.create(name=name, category_id=cat[0].id, price=price, description=description)
        # Перенаправляем на список товаров
        return redirect('product_list')  # Имя маршрута списка товаров
    # Если GET-запрос, отображаем форму
    return render(request, 'catalog/add_product.html')


def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных

    # Создаём пагинатор (10 товаров на страницу)
    paginator = Paginator(products, 10)

    # Получаем текущую страницу из запроса
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/product_list.html', {'page_obj': page_obj})


class IndexView(View):

    def get(self, request):
        return HttpResponse("Добро пожаловать в интернет-магазин!")

    def post(self, request):
        return HttpResponse("Данные отправлены.")






