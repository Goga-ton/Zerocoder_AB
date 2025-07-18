#Наследование
class Bird:
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет {self.voice}")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - раскраска")

class Pigeon(Bird):
# если мы хотим что-то добавить (расширить функционал коласса)
# тогда эта строка должна быть, иначе если хотим просто сдублировать вместо строки ниже пишем pass
    def __init__(self, name, voice, color, favorite_food):
# если мы хотим что-то добавить тогда эта строка должна быть
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):   # Данной функцией мы переопределили метод sing базового класса
        print(f"{self.name} поет плохо")

    def walk(self):
        print(f"{self.name} гуляет")

bird1 = Pigeon("Гоша", "баритон", "серый", "хлебные крошки")
bird2 = Bird("Стасян", "сопрано", "голубой")
bird1.sing()
bird1.info()
bird1.walk()
print(bird1.favorite_food)

