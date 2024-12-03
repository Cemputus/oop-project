class MenuItem:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available


class Drink(MenuItem):
    def __init__(self, name, price, available, size):
        super().__init__(name, price, available)
        self.size = size

    def order(self):
        print(f"Ordered Drink: {self.name}, Size: {self.size}, Price: {self.price}")


class Food(MenuItem):
    def __init__(self, name, price, available, is_vegetarian):
        super().__init__(name, price, available)
        self.is_vegetarian = is_vegetarian

    def order(self):
        print(f"Ordered Food: {self.name}, Vegetarian: {self.is_vegetarian}, Price: {self.price}")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def display_order(self):
        total_price = 0
        print("Order Details:")
        for item in self.items:
            print(f"- {item.name}: {item.price}")
            total_price += item.price
        print(f"Total Price: {total_price}")


# Demonstration
order = Order()
drink = Drink("Coke", 2.5, True, "Large")
food = Food("Pizza", 8.0, True, False)

order.add_item(drink)
order.add_item(food)

order.display_order()
