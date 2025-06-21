# test_products.py
import pytest
from products import Product, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Гаджеты и устройства", [sample_product])


def test_product_init(sample_product):
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Гаджеты и устройства"
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_count():
    initial_count = Category.category_count
    category = Category("Тест", "Тестовая категория", [])
    assert Category.category_count == initial_count + 1


def test_product_count():
    initial_count = Category.product_count
    product = Product("Тест", "Тестовый продукт", 100.0, 5)
    category = Category("Тест", "Тестовая категория", [product])
    assert Category.product_count == initial_count + 1


def test_add_product(sample_category):
    initial_count = Category.product_count
    new_product = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)
    sample_category.add_product(new_product)
    assert len(sample_category.products) == 2
    assert Category.product_count == initial_count + 1


def test_load_from_json(tmp_path):
    import json
    import os
    from products import load_from_json

    # Создаем временный JSON файл
    data = [
        {
            "name": "Электроника",
            "description": "Гаджеты",
            "products": [
                {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 50000.0,
                    "quantity": 10
                }
            ]
        }
    ]

    file_path = os.path.join(tmp_path, "test.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)

    categories = load_from_json(file_path)
    assert len(categories) == 1
    assert categories[0].name == "Электроника"
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "Телефон"