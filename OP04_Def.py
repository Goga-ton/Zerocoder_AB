#Функция сумирования
def sum():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a + b
    print("The sum is:", c)
sum()

#Функция определения цены с учетом скидки
def final_price(price, discount=10):
    result = price - (price * discount / 100)
    print(f"Цена с учетом скидки - {result}")
final_price(1500) #примениться скидка 10%
final_price(23000,27 ) #примениться скидка 27%

#Функция которая в цикле перебирает все имена и подставляет их в функцию
def hello(*names):
    print(names)
    for name in names:
        print("Hello", name)

hello("Alice", "Bob", "Charlie")

# Создание двух вункций def и расчет одной на основании другой
def cook(start_price):
    result_price = start_price + (start_price * 0.7)
    print("стоимость одной печеньки с наценкой", result_price)
    return result_price

def pack_price(cookie_price, cookie_count):
    result_price1 = cookie_price * cookie_count+57
    return result_price1

cook_price = cook(100)

pack = pack_price(cook_price, 10)
print('Стоимость пакета печенек с наценкой', pack)

#Видимость
def f():
    global text
    text = 'глобальная переменная'
    print('Внутри переменной находиться информация', text)

f()
print(text)

#Формирование списка через lambda с использованием функции filter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)

#Определение времени года
def season(month):
    if month >= 1 and month <= 12:
        if month == 12 or month == 1 or month == 2:
            return 'Зима'
            #print('Зима')
        elif month == 3 or month == 4 or month == 5:
            return 'Весна'
            #print('Весна')
        elif month == 6 or month == 7 or month == 8:
            return 'Лето'
            #print('Лето')
        else:
            return 'Осень'
            #print('Осень')
    else:
        print('Введен не правильный месяц')

a = int(input('Введи месяц - '))
result = season(a)
print(result)
