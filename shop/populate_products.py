from catalog.models import Category, Product


def populate_data():
    phones_category = Category.objects.get_or_create(name="Телефоны")[0]
    laptops_category = Category.objects.get_or_create(name="Ноутбуки")[0]

    Product.objects.create(
        name="iPhone 15",
        description="Смартфон Apple",
        price=120000,
        category=phones_category
        )
    Product.objects.create(
        name="MacBook Pro",
        description="Ноутбук Apple",
        price=250000,
        category=laptops_category
        )
    print("Данные успешно добавлены!")