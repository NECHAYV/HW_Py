import pytest
from main import Product, Smartphone, LawnGrass, Category


def test_product_addition_same_type():
    p1 = Product("Product1", "Desc1", 100, 10)
    p2 = Product("Product2", "Desc2", 200, 5)
    assert p1 + p2 == 100 * 10 + 200 * 5


def test_product_addition_different_types():
    smartphone = Smartphone("Phone", "Smart", 500, 3, "High", "X", "128GB", "Black")
    lawn_grass = LawnGrass("Grass", "Green", 50, 10, "Russia", "2 weeks", "Green")

    with pytest.raises(TypeError):
        smartphone + lawn_grass

    with pytest.raises(TypeError):
        lawn_grass + smartphone


def test_add_product_valid_type():
    category = Category("Electronics", "Devices")
    smartphone = Smartphone("Phone", "Smart", 500, 3, "High", "X", "128GB", "Black")
    category.add_product(smartphone)
    assert Category.total_products == 1


def test_add_product_invalid_type():
    category = Category("Electronics", "Devices")
    with pytest.raises(TypeError):
        category.add_product("Not a product")

    with pytest.raises(TypeError):
        category.add_product(123)


def test_smartphone_initialization():
    phone = Smartphone("Phone", "Smart", 500, 3, "High", "X", "128GB", "Black")
    assert phone.name == "Phone"
    assert phone.efficiency == "High"
    assert phone.model == "X"
    assert phone.memory == "128GB"
    assert phone.color == "Black"


def test_lawn_grass_initialization():
    grass = LawnGrass("Grass", "Green", 50, 10, "Russia", "2 weeks", "Green")
    assert grass.name == "Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == "2 weeks"
    assert grass.color == "Green"