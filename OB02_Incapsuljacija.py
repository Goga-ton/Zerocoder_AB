#Инкапсуляция1
class Test():
    def __init__(self):
        self.public = "Публичный атрибут"
        self._protected = "Защищенный атрибут"
        self.__private = "Приватный атрибут"

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value

test = Test()
print(test.public)
print(test._protected)
print(test.get_private())

test.set_private("Получили значение приватного атрибута")
print(test.get_private())

#Инкапсуляция2
class Test():
    def public_func(self):
        print("Публичный метод")
    def _protected_func(self):
        print("Защищенный метод")
    def __private_func(self):
        print("Приватный метод")
    def test_private(self):
        self.__private_func()

test = Test()
test.public_func()
test._protected_func()
test.test_private()

#Инкапсуляция3
class Car:
    def __init__(self, make, model):
        self.public_make = make #Открытый атрибут
        self._protec_model = model #Защищенный атрибут
        self.__private_year = 2022 #Приватный атрибут

    def public_metod(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protec_model}"
    def _protect_metod(selfself):
        return "Это защищенный метод"
    def __private_metod(selfself):
        return "Это приватный метод"

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        details = f"{self.public_make} {self._protect_model} Батарея: {self.battery_size} kWh."
        return details

tesla = ElectricCar('Tesla', 'Model S', 100)

print(tesla.public_make)
print(tesla.public_metod())

print(tesla._protec_model)
print(tesla._protect_metod())

#Доступ к приватному атрибуту и методу напрямую невозможен но Python
#позволяет обойти это ограничение (не рекомендуется):
print(tesla._Car__private_year)