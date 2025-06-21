# products.py
class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.__name = name
        self.__description = description
        self.__price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                confirm = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
                if confirm.lower() != 'y':
                    print("Изменение цены отменено")
                    return
            self.__price = new_price

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.__name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):

        if products:
            for product in products:
                if product.name.lower() == product_data['name'].lower():
                    # Обновляем существующий продукт
                    product.quantity += product_data['quantity']
                    if product_data['price'] > product.price:
                        product.price = product_data['price']
                    return product

        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Category:

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:

        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return CategoryIterator(self.__products)


class CategoryIterator:


    def __init__(self, products: list):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration