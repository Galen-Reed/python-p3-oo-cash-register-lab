#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, amount=1):
    for _ in range(amount):
      self.items.append(title)
    self.last_transaction = price * amount
    self.total += price * amount

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = int(self.total * (self.discount / 100))
      self.total -= discount_amount
      print(f'After the discount, the total comes to ${self.total}.')
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_transaction
    if self.last_transaction > 0:
      items_to_remove = int(self.last_transaction // (self.last_transaction / len(self.items)))
      for _ in range(items_to_remove):
        self.items.pop()
    pass
