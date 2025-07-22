#Задача №1
#Создайте класс Animal с методом make_sound(). Затем создайте несколько
# дочерних классов (например, Dog, Cat, Cow), которые наследуют Animal,
# но изменяют его поведение (метод make_sound()). В конце создайте список
# содержащий экземпляры этих животных и вызовите make_sound() для каждого
# животного в цикле.
import math


class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("I am a Dog")

class Kat(Animal):
    def make_sound(self):
        print("I am a Kat")

class Cow(Animal):
    def make_sound(self):
        print("I am a Cow")
animals = [Dog(), Kat(), Cow()] #создаем список не из элементов а из класов
for animal in animals:
    animal.make_sound()

#Задача №2
# Продемонстрировать принцип полиморфизма через реализацию разных классов,
# представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle,
# Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Share:
    def area(self):
        return 0

class Circle(Share):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Share):
    def __init__ (self, widht, height):
        self.width = widht
        self.height = height

    def area(self):
        return self.width * self.width

class Square(Share):
    def __init__ (self, widht):
        self.width = widht

    def area(self):
        return self.width ** 2

def print_area(shape):
    print(f"Площадь {shape.area()}")

circle = Circle(5)
print_area(circle)
rectangle = Rectangle(5, 6)
print_area(rectangle)
square = Square(7)
print_area(square)
#Если в коде выше убрать родительский клас у подкласов а сам родитель закоментить,
# прога все равно будет работать.

#Задача №3
#Создайте класс Author и класс Book. Класс Book должен использовать композицию для
# включения автора в качестве объекта.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f"{self.title} - {self.author.name} он {self.author.nationality}")

author = Author("Лев Толстой", "Русский")
book = Book("Война и мир", author)
book.get_info_book()
print(author.name)
