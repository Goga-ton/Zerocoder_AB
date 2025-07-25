class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.product = {}

    def add_product(self, title, price):
        self.product[title] = price

    def del_product(self,title):
        del self.product[title]

    def get_product(self,title):
        return self.product.get(title)

store1 = Store("Пятерочка", "Ленина, 5")
store1.add_product("Яблоко", 100)
store1.add_product("Вишня", 400)
store1.add_product("Арбуз", 250)

store2 = Store("Дикси", "Интернациональная, 17")
store2.add_product("Картошка", 60)
store2.add_product("Кукуруза", 85)

store3 = Store("Лента", "Гагарина, 28")
store3.add_product("Тыква", 180)
store3.add_product("Патиссон", 120)

print(f"Магазин '{store1.name}' расположенный по адресу: {store1.address} "
      f"\nИмеет ассортимент:\n {store1.product}")
print(f"Магазин '{store2.name}' расположенный по адресу: {store2.address} "
      f"\nИмеет ассортимент:\n {store2.product}")
print(f"Магазин '{store3.name}' расположенный по адресу: {store3.address} "
      f"\nИмеет ассортимент:\n {store3.product}")

store1.add_product("Арбуз", 800)
print()
print(store1.name)
print(f"Новая ценаs Арбуза - {store1.get_product("Арбуз")}")

print(f"\nСтоимость искомого товара Кукурузы - {store2.get_product("Кукуруза")}")

store3.del_product("Патиссон")
print(f"\nМагазин '{store3.name}' расположенный по адресу: "
      f"{store3.address} \nОставшийся ассортимент:\n {store3.product}")
