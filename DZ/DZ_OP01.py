# Урок ОР01 задание №1 "Калькулятор"
number_1 = int(input('Введите первое число - '))
number_2 = int(input('Введите второе число - '))
print(f'Умножение = {number_1*number_2}')
print(f'Деление = {number_1/number_2}')
print(f'Сложение = {number_1+number_2}')
print(f'Вычитание = {number_1-number_2}')
print(f'Возведение в степень = {number_1**number_2}')
print(f'Получение целой части при делении = {number_1//number_2}')
print(f'Получение остатка при делении = {number_1%number_2}')
print()
# Урок ОР01 задание №2 "Имя и возраст"
name = input('Как тебя зовут - ')
age = int(input('Сколько тебе лет - '))
print(f'Привет {name}! Тебе - {age} лет.')
print(f'Ты прожил(а) - {age*12} месяцев, {age*365} дней {age*365*24} часов')
print()
# Урок ОР01 задание №3 "Строки"
stroka_1 = input('Введите "Меня зовут Никто" - ')
stroka_2 = input('Введите "и я пришел ниоткуда" - ')
print(stroka_1 + " " + stroka_2)
print()
# Урок ОР01 задание №4 "Площадь прямоугольника"
dlina = int(input('Введите длину  прямоугольника - '))
shirina = int(input('ВВедите ширину прямоугольника - '))
print(f'Площядь прямоугольника = {dlina*shirina}')
print()
# Урок ОР01 задание №5 "Конвертация валюты"
valuta_1 = int(input('Введите количество денег которое хотите конвертировать  - '))
kyrs = float(input('Введите курс  - '))
valuta_2 = valuta_1/kyrs
print(f'Вы получите {valuta_2} условных едениц после конвертации')