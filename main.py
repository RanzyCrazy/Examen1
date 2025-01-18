
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price} UAH, Category: {self.category}"


class FoodItem(MenuItem):
    def __init__(self, name, price, category, calories):
        super().__init__(name, price, category)
        self.calories = calories

    def get_info(self):
        return super().get_info() + f", Calories: {self.calories}"

class DrinkItem(MenuItem):
    def __init__(self, name, price, category, size):
        super().__init__(name, price, category)
        self.size = size

    def get_info(self):
        return super().get_info() + f", Size: {self.size}"

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "pending"

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def set_status(self, status):
        self.status = status

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Status: {self.status}")
        print("Items ordered:")
        for item in self.items:
            print(item.get_info())
        print(f"Total price: {self.calculate_total()} UAH")


food1 = FoodItem("Pasta", 120, "food", 350)
food2 = FoodItem("Burger", 90, "food", 450)
drink1 = DrinkItem("Coke", 50, "drink", "M")
drink2 = DrinkItem("Juice", 60, "drink", "L")


order = Order(1)

order.add_item(food1)
order.add_item(food2)
order.add_item(drink1)
order.add_item(drink2)


order.display_order()


order.set_status("preparing")
order.display_order()


order.add_item(DrinkItem("Tea", 40, "drink", "S"))
order.display_order()


order.set_status("completed")
order.display_order()
