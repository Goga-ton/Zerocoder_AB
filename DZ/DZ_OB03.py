# Домашка к уроку OB3
class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return f"Тип: {self.name}, Возраст: {self.age}"
    def make_sound(self):
        pass
    def eat (self):
        pass

class Bird(Animal):
    def __init__ (self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def __str__ (self):
        return super().__str__() + f" Цвет: {self.color}"
    def make_sound(self):
        print("Пение птиц")
    def eat (self):
        print("Поедание зерен")

class Mammal(Animal):
    def __init__ (self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed
    def __str__ (self):
        return super().__str__() + f" Скорость: {self.speed} км/ч"
    def make_sound(self):
        print("Блеенье, мычание, вой и рык")
    def eat(self):
        print("Поедание травы или тех кто ее ест")

class Reptile(Animal):
    def __init__ (self, name, age, type_food):
        super().__init__(name, age)
        self.type_food = type_food
    def __str__ (self):
        return super().__str__() + f" Тип питания: {self.type_food}"
    def make_sound(self):
        print("Шипение")
    def eat (self):
        print("Пища зависит от типа рептилии и предпочтения")

bird1 = Bird('Воробей', 2, "Серый")
bird2 = Bird('Ворор', 50, "Черный")
mammal1 = Mammal('Лошадь', 5, 80)
mammal2 = Mammal('Лиса', 3, 15)
reptile1 = Reptile('Крокодил', 6, "Плотоядный")
reptile2 = Reptile('Ящерица', 1, "Всеядная")
animals = [bird1, bird2, mammal1, mammal2, reptile1, reptile2]
for an in animals:
    print(an)
    an.make_sound()
    an.eat()
print()

class Employee:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}, национальность: {self.nationality}."

class ZookKeeper(Employee):
    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)
        self.position = "Кормитель"
    def __str__(self):
        return super().__str__() + f" Спецификация: {self.position}."
    def feed_animal(self):
        print(f"{self.name} кормит животных.")

class Veterinarian(Employee):
    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)
        self.position = "Ветеринар"
    def __str__(self):
        return super().__str__() + f" Спецификация: {self.position}."
    def heal_animal(self):
        print(f"{self.name} лечит животных.")


class Zoo:
    def __init__ (self, name):
        self.name = name
        self.employees = []
        self.animals = []

    def add_employee (self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} принят на работу в {self.name}")

    def add_animal (self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} доставлено в {self.name}")

mammal3 = Mammal("Лев Симба", 5, 60)

people1 = Employee("Стас",24, "Русский")
people2 = Employee("Виктор Иванович",54, "Русский")
people3 = Employee("Люси",35, "Француженка")
people4 = ZookKeeper("Педро",31, "Месиканец")
people5 = Veterinarian("Ханна",42, "Немка")

# people4.feed_animal()
# people5.heal_animal()

my_zoo = Zoo("Зоопарк 'Райский уголок'")
my_zoo.add_animal(bird1)
my_zoo.add_animal(bird2)
my_zoo.add_animal(reptile2)
my_zoo.add_animal(mammal1)
my_zoo.add_animal(mammal3)
print()
my_zoo.add_employee(people1)
my_zoo.add_employee(people2)
my_zoo.add_employee(people3)
my_zoo.add_employee(people4)
my_zoo.add_employee(people5)
print()
for an in my_zoo.animals:
    print(an)

for em in my_zoo.employees:
    print(em)
    #print(f"{em.name} {em.age} {em.nationality} {em.position}")