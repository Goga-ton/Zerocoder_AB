#Задание #1
print('Вводишь предложения и они сохраняются в файл\n')
text = input('Введи текс, пару не длинных предложений: ')
with open('../user_data.txt', 'w') as fl:
    fl.write(text)
with open('../user_data.txt') as fl:
    print(fl.read())


# Задание #2
print('\nПодтягиваешь математические функции из другого файла\n')
from arithmetic import sum, minus, dele, umn

a = input('Enter a number: ')
b = input('Enter a number: ')

result = sum(int(a), int(b))
print('Результат сложения - ', result )

result = minus(int(a), int(b))
print('Результат вычитания - ', result )

result = dele(int(a), int(b))
print('Результат деления - ', result )

result = umn(int(a), int(b))
print('Результат умножения - ', result )


#Задание 3
from random import choice
print('\nВыбираем 5 уникальных имен из списка, случайным образом\n')

spis_name = ['Антон','Сергей','Даша','Матвей','Игорь','Лена','Лида','Светогор','Тома','Артем',]
#print(spis_name.count('Сергей'))

spis_name5 = []
for i in range(5):
    i = choice(spis_name)
    #spis_name5.append(i)

    #Удаление через "del" (через индекс в списке)
    spis_name5.append(i)
    x = spis_name.index(i)
    del spis_name[x]

    # Удаление через "pop" (через индекс в списке b присвоение удаленного значения новой переменной)
    #x = spis_name.index(i)
    #a = spis_name.pop(x)
    #spis_name5.append(a)

    #Удаление через "remove" (по наименованию в списке)
    #spis_name5.append(i)
    #spis_name.remove(i)

print(spis_name5)
print(spis_name)


#Задание 3 - решали на следующем уроке
import random
students = ["Алексей", "Иван", "Мария", "Екатерина", "Павел", "Анна", "Даниил", "Наталья", "Сергей", "Виктория"]
random_students = random.sample(students, 5)
print("Имена учеников, которые будут отвечать на уроке:")

for student in random_students:
    print(student)