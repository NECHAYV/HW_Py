class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def average_price(self):
        try:
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0