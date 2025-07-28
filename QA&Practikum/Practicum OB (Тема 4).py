class Personal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def __str__(self):
    #     return f'{self.name} is {self.age} years old'
    def say_hi(self, name):
        return f"Привет {name}! Меня зовут {self.name} мне {self.age} лет."

class Professor(Personal):
    def __init__(self, name, age, years):
        super().__init__(name, age)
        self.years = years
    def say_hi(self, name):
        return super().say_hi(name) + f"Мой стаж {self.years} лет."

# print(Personal('Anton', 25))
# personal1 = Personal("Жора", 28)
# print(personal1.name, personal1.age)
# print(personal1.say_hi("Малибу"))

personal2 = Professor("Сергей Иванович", 56, 15)
print(personal2.say_hi("Люси"))