#Использование ошибок для не остановки программы
try:
    # Запрашиваем у пользователя два числа
    numerator = float(input("Введите числитель: "))
    denominator = float(input("Введите знаменатель: "))
    # Выполняем деление
    result = numerator / denominator
    # Выводим результат
    print("Результат деления:", result)
except ZeroDivisionError:
    # Обработка ошибки деления на ноль
    print("Ошибка: на ноль делить нельзя!")
except ValueError:
    # Обработка ошибки ввода, если введено не число
    print("Ошибка: введено не число.")
# Можно объеденять ошибки
# except (ZeroDivisionError, ValueError) as e:
# print("Ошибка: ", e)


# Позволяет видеть полное название ошибки
try:
    print('3' + 2)
except Exception as e:
    print('Произошла ошибка: ', e)


# Вариант когда будет ловиться оюбая ошибка и не останавливать программу а переходит к следующей мтроке
# в нашем случаи это сообщения
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Преобразование в число не сработало")

print("Конец программы")


#Разбор ситуации с else
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Преобразование в число не сработало")
else:
    print('Трай выполнился без ошибок')
finally: #Строка которая будет выполняться при любор раскладе
    print("Выполнить в любом случаи")

print("Конец программы")


#Работа со списками, в try добавляем только ту часть кода которая может вызывать ошибку
my_list = [10, 20, 30, 40, 50]
index = int(input(('Введите индекс - ')))
try:
    print(my_list[index])
except IndexError:
    print('Такого элемента нет')


#Ошибки которые создает пользователь
class MyCustomError(Exception): # (Exception) - базовый клас для пользовательский исключений
    pass #Просто закрываем блок
def chec_number(x):
     if x>100:
         raise MyCustomError('Число больше 100') #Генерируем ошибку, т.е. описываем ее условия
     elif x<0:
         raise MyCustomError('Число меньше 0')
     else:
         print('Число в диапозоне')

try:
    chec_number(-5)
except MyCustomError as e:
    print(e)