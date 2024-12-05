
### Question 4


##### part A
# Creating a Base class MenuItem
class MenuItem:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available
        
        
 # This will be overridden in the derived classes
    def order(self):
        pass


# Derived class Drink
class Drink(MenuItem):
    def __init__(self, name, price, available, size):
        super().__init__(name, price, available)
        self.size = size

    def order(self):
        return f"Drink: {self.name} (Size: {self.size}) - SHS {self.price:.2f}"


# Derived class Food
class Food(MenuItem):
    def __init__(self, name, price, available, is_vegetarian):
        super().__init__(name, price, available)
        self.is_vegetarian = is_vegetarian

    def order(self):
        vegetarian_status = "Vegetarian" if self.is_vegetarian else "Non-Vegetarian"
        return f"Food: {self.name} ({vegetarian_status}) - SHS {self.price:.2f}"


### part c
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item.available:
            self.items.append(item)
            print(f"Added: {item.name} to the order.")
        else:
            print(f"{item.name} is not available.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed: {item.name} from the order.")
        else:
            print(f"{item.name} is not in the order.")
## Part d
    def display_order(self):
        if not self.items:
            print("Your order is empty.")
        else:
            total_price = 0
            print("Welcome to CEN restaurant\n   Your order details:")
            
            for item in self.items:
                print(item.order())
                total_price += item.price
            print(f"Total Price: SHS {total_price:.2f}")



# Creating the  menu items (Drinks and Foods)

drink1 = Drink("Minute Maid", 2500, True, "Medium")
drink2 = Drink("Pepsi", 5000, True, "Large")
food1 = Food("Pizza", 28000, True, False)
food2 = Food("Matooke amd Meat", 15000, True, True)


order = Order()


order.add_item(drink1)
order.add_item(food1)
order.add_item(drink2)

order.remove_item(food2)  
order.remove_item(food1) 

order.display_order()
