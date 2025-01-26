# module_18

**_Установка_**
`pip install django`\
**_Создание проекта Джанго_**\
`django-admin startproject UrbanDjango`\
**_Запуск локального сервера_**\
`python manage.py runserver`\
**_Создание приложения_**\
`python manage.py startapp <имя приложения>`\
**_Создание таблиц в базе данных_**\
`python manage.py migrate`

**_Проверка проекта на ошибки_**\
`python manage.py check`
**_Список доступных команд_**\
`python manage.py help`
`pip freeze >> requirements.txt`

`django-admin --version`

● Model (Модель): хранит данные.
● View (Представление): логика обработки запроса.
● Template (Шаблон): отвечает за отображение данных в удобном формате.

**_Создание админа_**\
`python manage.py createsuperuser`

Миграции синхронизируют изменения в моделях с базой данных.
Создание миграций

`python manage.py makemigrations`

**_Создание таблиц в базе данных_**\
`python manage.py migrate`

Операции с Django ORM выполняются в:

1. Django Shell (интерактивный интерфейс).
2. Представлениях (views) — если операции связаны с пользовательскими запросами.
3. Скриптах миграций или тестах — для автоматизации задач или тестирования.

`python manage.py shell`

```commandline
from catalog.models import Product
products=Product.objects.all()
print(products)

expensive_products=Product.objects.filter(price__gte=130000)
for p in expensive_products:
    print(p.name, p.price)
```

Операторы для фильтрации:

field__exact — точное совпадение (price__exact=50000).
field__icontains — поиск по подстроке без учета регистра (name__icontains="iphone").
field__gte / field__lte — больше/меньше или равно (price__gte=50000).

Метод order_by() сортирует записи

```commandline
sorted_products = Product.objects.order_by('-price') # По убыванию цены
for product in sorted_products:
print(product.name, product.price)
```

Агрегация данных

```commandline
from catalog.models import Product
from django.db.models import Avg, Min, Max, Count
stats = Product.objects.aggregate(
avg_price=Avg('price'),
min_price=Min('price'),
max_price=Max('price'),
total_products=Count('id')
)
print(stats)
```

Аннотации данных

```commandline
from catalog.models import Product
from django.db.models import F, DecimalField, ExpressionWrapper
discounted_products = Product.objects.annotate(
discounted_price=ExpressionWrapper(
F('price') * 0.9,
output_field=DecimalField()
)
)
for product in discounted_products:
print(product.name, product.discounted_price)
```

Получение всех товаров категории

```commandline
from catalog.models import Category
category = Category.objects.get(name="Телефоны")
products = category.product_set.all()
for product in products:
print(product.name)
```

Чтобы немного упростить импорты, можно импортировать через *

```commandline
from catalog.models import *
category = Category.objects.get(name="Телефоны")
products = category.product_set.all()
for product in products:
print(product.name)
```

**Создание данных для работы с QuerySet**

_Используйте админ-панель Django или Shell:_

```commandline
phones_category = Category.objects.create(name="Телефоны")
Product.objects.create(
name="Samsung Galaxy",
description="Смартфон Samsung",
price=75000,
category=phones_category
)
```

_Проверка данных перед вызовом get()_
```commandline
if Product.objects.filter(name="iPhone 14").exists():
    product = Product.objects.get(name="iPhone 14")
else:
    print("Товар не найден")
```