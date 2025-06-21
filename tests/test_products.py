# test_products.py
import pytest
from products import Product, Category, CategoryIterator


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def another_product():
    return Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)


@pytest.fixture
def sample_category(sample_product, another_product):
    return Category("Электроника", "Гаджеты и устройства", [sample_product, another_product])


def test_product_str(sample_product):
    assert str(sample_product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_category_str(sample_category):
    assert str(sample_category) == "Электроника, количество продуктов: 15 шт."
    assert "количество продуктов: 15 шт." in str(sample_category)


def test_product_addition(sample_product, another_product):
    total = sample_product + another_product
    assert total == 50000.0 * 10 + 100000.0 * 5


def test_product_addition_type_error(sample_product):
    with pytest.raises(TypeError):
        sample_product + 100


def test_category_iterator(sample_category):
    products = list(sample_category)
    assert len(products) == 2
    assert isinstance(products[0], Product)
    assert products[0].name == "Телефон"
    assert products[1].name == "Ноутбук"


def test_category_iterator_empty():
    empty_category = Category("Пустая", "Нет товаров", [])
    products = list(empty_category)
    assert len(products) == 0


def test_category_iterator_loop(sample_category):
    names = [product.name for product in sample_category]
    assert names == ["Телефон", "Ноутбук"]