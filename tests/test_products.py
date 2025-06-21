def test_add_product_with_check():
    category = Category("Тест", "Тестовая категория")
    product = Product("Тест", "Тестовый продукт", 100, 10)


    category.add_product(product)
    assert Category.total_products == 1


    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_private_price():
    product = Product("Тест", "Тест", 100, 10)


    with pytest.raises(AttributeError):
        print(product.__price)


    assert product.price == 100


    product.price = 150
    assert product.price == 150


    product.price = -50
    assert product.price == 150