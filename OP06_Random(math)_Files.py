#модуль random
from random import randint, random, choice, randrange, shuffle

result = random()
print(f"результат - {result}")

result = randint(1, 10)
print(f"результат - {result}")

my_list = ["яблоко", "банан", "вишня", "клубника", "апельсин"]
result = choice(my_list)
print(f"результат - {result}")

result1 = randrange(1,123,5)
print(f"результат - {result1}")

shuffle(my_list)
print(f"результат - {my_list}")
print()


#Напишите простую программу, которая генерирует случайный пароль длиной 8 символов.
#Пароль должен содержать случайно выбранные строчные и заглавные буквы, цифры и специальные символы.
# Используйте модуль random для выбора символов.
import random
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%~&*()_+="
password = ""
for i in range(8):
    password += random.choice(letters)
print(password)


#модуль math
import math

radius = float(input("введите радиус круга - "))
area = math.pi * radius ** 2
print(f"Плoшaдь кругa - {area}")

katetA = float(input("введите катет 1  - "))
katetB = float(input("введите катет 2 - "))
gipot = math.sqrt(math.pow(katetA,2)+math.pow(katetB,2))
print("Гипотенуза равна - ", gipot)


#Работа с файлами
#Первый вариант работы с файлами который не требует их закрытия
with open('new_text_file.txt', 'r') as file:
    print(file.read())

with open('new_text_file.txt', 'r') as file:
    for line in file:
        print(line + 'Это строка обработанна циклом For')

    #file.write('\nДобавляем все разобрались')
    #print(file.read())

#Второй вариант работы с файлами который требует их закрытия
print()
file = open('new_text_file.txt', encoding='utf-8')
text1 = file.read()
text2 = file.read(12)
print(text1)
print(text2)
file.close()

