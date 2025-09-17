# JAI.py
class BStore:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty): 
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total 


b = BStore()
b.add_item("papaya", 100)
b.add_item("Guava", 200)
b.add_item("Orange", 150)


print("Current Items in BookShop:")
for item in b.items:
    print(item[0], "=", item[1])

total_qty = b.calculate_total()
print("Total Quantity:", total_qty)

b.remove_item("Guava")

print("Items after removing Guava:")
for item in b.items:
    print(item[0], "-", item[1])

total_qty = b.calculate_total()
print("Total Quantity:", total_qty)



