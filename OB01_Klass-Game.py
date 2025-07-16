# Сщздаем Класс - Воин и два объекта Воин 1 и Воин 2. Воины имеют Атрибуты (Свойства): Имя, Сила, Выносливость, Цвет волос и
# методы (действия) : спать, есть, бить и ходить. Описываем что происходит с Атрибутами при конкретных Методах
class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance +=2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power +=1

    def hit(self):
        print(f"{self.name} бъет врага")
        self.endurance -=6

    def walk(self):
        print(f"{self.name} гуляет")


    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвето волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость воина - {self.endurance}")

war1 = Warrior("Степан", 76, 54, "Коричневый")
war2 = Warrior("Егор", 45, 23, "Блондин")

war1.info()
war1.sleep()
war1.eat()
war1.hit()
war1.walk()
print(war1.power)
print(war1.endurance)

war2.info()
war2.sleep()
war2.eat()
war2.hit()
war2.walk()
print(war2.power)
print(war2.endurance)

#print(war1.endurance)
#war1.sleep()
#print(war1.endurance)

#print(war2.name)
#print(war2.power)
#print(war2.endurance)
#print(war2.hair_color)
#print()



