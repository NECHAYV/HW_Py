from abc import ABC, abstractmethod
class LogMixin:

    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        for i, arg in enumerate(args):
            print(f"  Параметр {i + 1}: {arg}")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):


    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, LogMixin):


    def __init__(self, name, description, price, quantity):
        super().__init__(name=name, description=description, price=price, quantity=quantity)
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class OrderBase(ABC):


    @abstractmethod
    def __init__(self):
        self.items = []

    @abstractmethod
    def total_cost(self):
        pass


class Order(OrderBase):


    def __init__(self, product, quantity):
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.items.append(product)

    def total_cost(self):
        return self.product.price * self.quantity


class Category(OrderBase):

    total_products = 0

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.total_products += 1
        self.items.append(product)

    def total_cost(self):
        return sum(p.price * p.quantity for p in self.__products)

    @property
    def products(self):
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return ''.join(products_list)