class ShoppingCart:
  def __init__(self):
    self.items=[]
  def add_item(self,name,price):
    self.items.append({"name":name,"price":price})
  def total(self):
    total_price=0
    for item in self.items:
      total_price+=item["price"]
    return total_price
  def show_items(self):
    for item in self.items:
      print(f"{item["name"]}:{item["price"]}")
    #return self.items
  def remove_item(self,name):
    for item in self.items:
      if item["name"]==name:
        self.items.remove(item)
        return
      
cart=ShoppingCart()
cart.add_item("Apple",1.50)
cart.add_item("bread", 3.00)

print(cart.total())
print()
cart.show_items()
print()
cart.remove_item("bread")
print (cart.show_items())

print("hello world")

