# test_products.py
import pytest
from products import Product, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Гаджеты и устройства", [sample_product])


def test_private_attributes(sample_product, sample_category):
    # Проверка приватных атрибутов Product
    assert hasattr(sample_product, '_Product__name')
    assert hasattr(sample_product, '_Product__price')

    # Проверка приватного атрибута Category
    assert hasattr(sample_category, '_Category__products')


def test_add_product(sample_category):
    initial_count = Category.product_count
    new_product = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)
    sample_category.add_product(new_product)
    assert len(sample_category.products.split('\n')) == 2
    assert Category.product_count == initial_count + 1


def test_products_property(sample_category, sample_product):
    products_str = sample_category.products
    assert str(sample_product) in products_str
    assert "руб." in products_str
    assert "Остаток:" in products_str


def test_new_product_classmethod():
    product_data = {
        'name': 'Планшет',
        'description': 'Графический планшет',
        'price': 30000.0,
        'quantity': 3
    }
    product = Product.new_product(product_data)
    assert product.name == 'Планшет'
    assert product.price == 30000.0
    assert product.quantity == 3


def test_new_product_update_existing():
    existing_product = Product("Мышь", "Компьютерная мышь", 1500.0, 10)
    product_data = {
        'name': 'мышь',
        'description': 'Новое описание',
        'price': 2000.0,
        'quantity': 5
    }
    updated_product = Product.new_product(product_data, [existing_product])
    assert updated_product.quantity == 15
    assert updated_product.price == 2000.0


def test_price_setter(sample_product, capsys):
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 50000.0

    sample_product.price = 60000.0
    assert sample_product.price == 60000.0


def test_price_decrease_confirmation(sample_product, monkeypatch):
    # Тестирование подтверждения снижения цены
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    sample_product.price = 40000.0
    assert sample_product.price == 40000.0

    # Тестирование отмены снижения цены
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    sample_product.price = 30000.0
    assert sample_product.price == 40000.0  # Цена не изменилась