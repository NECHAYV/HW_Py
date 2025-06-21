class Category:
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []

    def add_product(self, product):

        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):

        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return ''.join(products_list)

    @classmethod
    def new_product(cls, product_data, products_list=None):

        if products_list is not None:
            for existing_product in products_list:
                if existing_product.name == product_data['name']:

                    existing_product.quantity += product_data['quantity']

                    if product_data['price'] > existing_product.price:
                        existing_product.price = product_data['price']
                    return existing_product


        return Product(**product_data)


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):

        return self.__price

    @price.setter
    def price(self, new_price):

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:

            if hasattr(self, '_Product__price') and new_price < self.__price:
                confirmation = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
                if confirmation.lower() != 'y':
                    print("Изменение цены отменено")
                    return
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data):

        return cls(**product_data)