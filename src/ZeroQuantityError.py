class ZeroQuantityError(Exception):
    pass

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        try:
            if quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
            self.quantity = quantity
        except ZeroQuantityError as e:
            print(e)
            raise
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")