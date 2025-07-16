class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.product = []

    def add_product(self, title, price):
        self.product.append({"title":title, "price":price})


    #def remove_product(self, product):
store1 = Store("Пятерочка", "Ленина, 5")
store2 = Store("Дикси", "Интернациональная, 17")
store3 = Store("Лента", "Гагарина, 28")
store1.add_product("Яблоко", 100)
store1.add_product("Вишня", 400)


print(store1.name, store1.address, store1.product)
print(store2.name, store2.address, store2.product)
print(store3.name, store3.address, store3.product)