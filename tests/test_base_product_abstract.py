import pytest
from main import BaseProduct, Product, Smartphone, LawnGrass, Order, Category

def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100, 1)

def test_product_creation_logging(capsys):
    p = Product("Test", "Desc", 100, 1)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "Параметр 1: Test" in captured.out

def test_order_creation():
    p = Product("Test", "Desc", 100, 1)
    order = Order(p, 2)
    assert order.total_cost() == 200
    assert len(order.items) == 1

def test_category_total_cost():
    cat = Category("Test", "Desc")
    p1 = Product("P1", "Desc1", 100, 2)
    p2 = Product("P2", "Desc2", 200, 1)
    cat.add_product(p1)
    cat.add_product(p2)
    assert cat.total_cost() == 400

def test_order_base_abstract():
    with pytest.raises(TypeError):
        OrderBase()

def test_product_inheritance():
    assert issubclass(Product, BaseProduct)
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)

def test_order_category_inheritance():
    assert issubclass(Order, OrderBase)
    assert issubclass(Category, OrderBase)