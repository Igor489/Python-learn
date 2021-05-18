class Store:
    def __init__(self):
        self.store = []


class Entity:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Entity):
    def __init__(self, name, price, print_size):
        super().__init__(name, price)
        self.print_size = print_size


class Scanner(Entity):
    def __init__(self, name, price, is_color):
        super().__init__(name, price)
        self.is_color = is_color


class Copier(Entity):
    def __init__(self, name, price, is_multipage):
        super().__init__(name, price)
        self.is_multipage = is_multipage
