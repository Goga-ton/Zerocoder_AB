#Урок ОР03
# Задание №1
print ('Урок ОР03')
print ('Задание №1 (Поиск наименьшего числа)')
spisok = []
for i in range(3):
    data = input(f'Введите число {i+1}: ')
    spisok.append(data)
spisok_min = min(spisok)
print('Минимальное число из введеных Вами = ' + spisok_min)


# Задание №2
print ('Задание №2 (Калькулятор)')

a = float(input('Введите число a - '))
b = float(input('Введите число b - '))
print('Перечень математических операций:')
print('1. Сложение (+)')
print('2. Вычитание (-)')
print('3. Умножение (*)')
print('4. Деление (/)')
print('5. Возведение в степень (**)')
print('6. Деление без остатка (//)')
print('7. Получение остатка при делении (%)')

while True:
    print('Для выхода введи "0"')
    znak = input('Выбери математическое действие: ')
    if znak == '0': break
    if znak == '1':
        print(f'Сумма = {a+b}')
    elif znak == '2':
        print(f'Разница = {a-b}')
    elif znak == '3':
        print(f'Произведение = {a*b}')
    elif znak == '4':
        print(f'Частное = {a/b}')
    elif znak == '5':
        print(f'"a" в встепени "b" = {a**b}')
    elif znak == '6':
        print(f'Целое Частное = {a//b}')
    elif znak == '7':
        print(f'Остаток от частного = {a%b}')

    else:
        print('Вы выбрали недопустимое математическсое действие')
        break

# Задание №3
print ('Задание №3 (Определение кол-ва дней в месяце)')
a = int(input('Введите число месяца - '))
if a>12 or a<1:
    print('Вы ввели несуществующий месяц')
elif a==2:
    print('В данном месяце 28 дней')
elif a%2==0 and 2<a<8:
   print('В данном месяце 30 день')
elif a%2!=0 and 2<a<8:
    print('В данном месяце 31 день')
elif a%2!=0 and a>=8:
    print('В данном месяце 30 день')
else:
   print('В данном месяце 31 день')

# Задание №4
print ('Задание №4 (Вывести четные числа из списка)')
start = int(input('Введите число с которого хотите начать список: '))
end = int(input('Введите число которым хотите закончить список: '))
numbers = list(range(start, end + 1))
#print(numbers)
print('Данный список содержит следующте четные числа: ')
for number in numbers:
    if number % 2 == 0:
        print(number)

# Задание №5
print ('Задание №1 (Поиск наименьшего числа)')
games=['камень', 'ножницы', 'бумага']
import random
P = 0
U = 0

while P<3 and U<3:
    pc = random.choice(games)
    unit = input('Введите свое значение (камень/ножницы/бумага): ')
    if unit.lower() in games:
        if pc==unit.lower():
            print("Компьютер тоже загадал " + unit + ", у Вас ничья. Попробуйте еще раз.")

        elif pc == "камень" and unit.lower() == "ножницы":
            P += 1
        elif pc == "камень" and unit.lower() == "бумага":
            U += 1

        elif pc == "ножницы" and unit.lower() == "камень":
            U += 1
        elif pc == "ножницы" and unit.lower() == "бумага":
            P += 1

        elif pc == "бумага" and unit.lower() == "камень":
            P += 1
        elif pc == "бумага" and unit.lower() == "ножницы":
            U += 1
        print('Компьютер загадал - ' + pc)
        print(f'P = {P}')
        print(f'U = {U}')

    else:
        print('Вы ввели неверное слово, попробуйте заново')
if P == 3:
    print(f"Вы прогиграли, компьютер набрал {P} очка")
else:
    print(f"Вы победили у Вас {U} очка")