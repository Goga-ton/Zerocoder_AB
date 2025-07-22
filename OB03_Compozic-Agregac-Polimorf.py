#Композиция
class Engine:
    def start(self):
        print("Двигатель запущен")
    def stop(self):
        print("Двигатель остановлен")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()

print ("\nTest:")
my_engine = Engine()
my_engine.start()
my_engine.stop()

#Агрегация
class Teacher:
    def teach(self):
        print("Преподователь учит")

class School:
    def __init__ (self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()
my_school = School(my_teacher)
my_teacher.teach()
my_school.start_lesson()

#Полиморфизм
class Dog:
    def speak(self):
        return "Wolf!"
class Kat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
kat = Kat()

animal_speak(dog)
animal_speak(kat)








