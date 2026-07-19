def total_price_1item(unit_price, quantity=1):
  total = unit_price * quantity
  return total

total_price = total_price_1item(quantity=20, unit_price=130)
print(total_price)

def total_price_1item(unit_price: int, quantity: int=1) -> str:
  total_price = unit_price * quantity
  return f'¥{total_price:,}'

total_price = total_price_1item(1300)
print(total_price)