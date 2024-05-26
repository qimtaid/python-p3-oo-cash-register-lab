#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            self.total -= self.total / len(self.items)
        else:
            self.total = 0
