import pytest


def test_product_zero_quantity():
    with pytest.raises(ValueError):
        Product("Test", 10, 0)


def test_category_average_price():
    category = Category("Test")
    assert category.average_price() == 0

    category.add_product(Product("Product1", 10, 5))
    category.add_product(Product("Product2", 20, 3))
    assert category.average_price() == 15