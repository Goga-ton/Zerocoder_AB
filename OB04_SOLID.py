#Пример кода который не соответсвует принципу №1 SOLID
# class UserManager:
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         file = open("user.txt", "a")
#         file.write(self.user)
#         file.close()

# Принцип №1 "S" - Единственной ответсвенности
class UserManager:
    def __init__(self, user):
        self.user = user

class UserNameChange:
    def __init__(self, user):
        self.user = user
    def change_name(self, new_name):
        self.user = new_name

class SaveUser:
    def __init__(self, user):
        self.user = user
    def save_user(self):
        file = open("user.txt", "a")
        file.write(self.user)
        file.close()

# Пример кода не соответсвующий Принцип №2 "O" (OCP - Open/Closed Principle) - Открытости/Закрытости
# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def docPrinter(self):
#         print(f"Сформирован отчет - {self.title} - {self.content}")
#
# rep = Report("Это название отчета", "Тут должно содержаться информации дофига - т.е очень много")
# rep.docPrinter()
# print(rep.title)

# Принцип №2 "O" (OCP - Open/Closed Principle) - Открытости/Закрытости
from abc import ABC, abstractmethod
class Formatted(ABC): #создаем абстрактный клас
    @abstractmethod
    def format(self, report):
        pass
class TextFormatted(Formatted):
    def format(self, report):
        print(report.tittle)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.tittle}</h1>")
        print(f"<p>{report.content}</p>")

class Report:
    def __init__(self, tittle, content, formatted):
        self.tittle = tittle
        self.content = content
        self.formatted = formatted #в formatted сохраняется объект класса либо HtmlFormatted либо TextFormatted

    def docPrinter(self):
        self.formatted.format(self) #вызываем функцию format  у характеристика formated

report  = Report("Заголовок отчета", "это текст отчета его тут много", TextFormatted())
report.docPrinter()


# Пример кода не соответсвующий Принципу №3 "L" (LSP - Liskov Substitution Principle) - Принцип Барбары Лисков
# class Bird:
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("Птица летает")
#
# class Ping(Bird):
#     pass
#
# p = Ping("Стася")
# print(p.name)
# p.fly()
#проблема кода выше в том что пингвин не летает но без переопределения класса мы этого сделать не сможем

#Принцип №3 "L" (LSP - Liskov Substitution Principle) - Принцип Барбары Лисков
class Bird:
    def fly(self):
        print("Эта птица летает")

class Duck(Bird):
    def fly(self):
        print("Эта утка летает быстро")

def fly_in_sky(animal):
    animal.fly()

b = Bird()
d = Duck()
fly_in_sky(b)
fly_in_sky(d)

#Пример кода не соответсвующий Принципу №4 разделения интерфейсов (ISP - Interface Segregation Principle)
# class SmartHouse:
#     def turn_on_lith(self):
#         pass
#     def heat_food(self):
#         pass
#     def play_music(self):
#         pass

#Принцип #4 разделения интерфейсов (ISP - Interface Segregation Principle)
class light:
    def turn_on(self):
        print("Свет включен")

class Food:
    def head_food(self):
        print("Еда началась разогреваться")

class Music:
    def play_music(self):
        print("Включаю подборку Ваших любимых песен")

#Пример кода не соответсвующий принципу №5 Инверсии зависимости (DIP, Dependency Inversion Principle)
# class Book:
#     def read(self):
#         print("Чтение интересной истории")
#
# class StoryReader:
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read() #используем функцию read из класса Book. Сейчас клас StoryReader очень сильно зависит от класса Book, так быть не должно
from _csv import Reader

#Принцип #5 Инверсии зависимости (DIP, Dependency Inversion Principle)
from abc import ABC, abstractmethod

class StorySourse(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySourse):
    def get_story(self):
        print("Чтение интересной книги")

class AudioBook(StorySourse):
    def get_story(self):
        print("Прослушивание интересной истории - Аудиокнига")

class StoryReader:
    def __init__(self, sroty_sourse: StorySourse):
        self.sroty_sourse = sroty_sourse

    def tell_story(self):
        self.sroty_sourse.get_story()

book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audiobook)

readerBook.tell_story()
readerAudioBook.tell_story()



