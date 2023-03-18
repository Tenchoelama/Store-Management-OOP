class Item:
    
    
    discount= 0.8 # The pay rate after 20% discount
    all_items = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all_items.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"#represents objects in string 

item1 = Item("Laptop", 100, 1)
item2 = Item("Guitar", 1000, 3)
item3 = Item("Gun", 10, 5)
item4 = Item("Bike", 50, 5)
item5 = Item("Sword", 75, 5)

print(Item.all_items)