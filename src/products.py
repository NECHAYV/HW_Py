class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity